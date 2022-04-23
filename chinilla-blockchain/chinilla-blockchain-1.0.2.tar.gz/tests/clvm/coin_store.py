from collections import defaultdict
from dataclasses import dataclass, replace
from typing import Dict, Iterator, Optional

from chinilla.full_node.mempool_check_conditions import mempool_check_time_locks, get_name_puzzle_conditions
from chinilla.types.blockchain_format.coin import Coin
from chinilla.types.blockchain_format.sized_bytes import bytes32
from chinilla.types.coin_record import CoinRecord
from chinilla.types.spend_bundle import SpendBundle
from chinilla.util.ints import uint32, uint64
from chinilla.full_node.bundle_tools import simple_solution_generator
from chinilla.util.errors import Err
from chinilla.consensus.cost_calculator import NPCResult


MAX_COST = 11000000000


class BadSpendBundleError(Exception):
    pass


@dataclass
class CoinTimestamp:
    seconds: int
    height: int


class CoinStore:
    def __init__(self, reward_mask: int = 0):
        self._db: Dict[bytes32, CoinRecord] = dict()
        self._ph_index: Dict = defaultdict(list)
        self._reward_mask = reward_mask

    def farm_coin(
        self,
        puzzle_hash: bytes32,
        birthday: CoinTimestamp,
        amount: int = 1024,
        prefix=bytes32.fromhex("ccd5bb71183532bff220ba46c268991a00000000000000000000000000000000"),  # noqa
    ) -> Coin:
        parent = bytes32(
            [
                a | b
                for a, b in zip(
                    prefix,
                    birthday.height.to_bytes(32, "big"),
                )
            ],
        )
        # parent = birthday.height.to_bytes(32, "big")
        coin = Coin(parent, puzzle_hash, uint64(amount))
        self._add_coin_entry(coin, birthday)
        return coin

    def validate_spend_bundle(
        self,
        spend_bundle: SpendBundle,
        now: CoinTimestamp,
        max_cost: int,
        cost_per_byte: int,
    ) -> int:
        # this should use blockchain consensus code

        program = simple_solution_generator(spend_bundle)
        result: NPCResult = get_name_puzzle_conditions(
            program, max_cost, cost_per_byte=cost_per_byte, mempool_mode=True
        )
        if result.error is not None:
            raise BadSpendBundleError(f"condition validation failure {Err(result.error)}")

        ephemeral_db = dict(self._db)
        assert result.conds is not None
        for spend in result.conds.spends:
            for puzzle_hash, amount, hint in spend.create_coin:
                coin = Coin(spend.coin_id, puzzle_hash, amount)
                name = coin.name()
                ephemeral_db[name] = CoinRecord(
                    coin,
                    uint32(now.height),
                    uint32(0),
                    False,
                    uint64(now.seconds),
                )

        err = mempool_check_time_locks(
            ephemeral_db,
            result.conds,
            uint32(now.height),
            uint64(now.seconds),
        )

        if err is not None:
            raise BadSpendBundleError(f"condition validation failure {Err(err)}")

        return 0

    def update_coin_store_for_spend_bundle(
        self,
        spend_bundle: SpendBundle,
        now: CoinTimestamp,
        max_cost: int,
        cost_per_byte: int,
    ):
        err = self.validate_spend_bundle(spend_bundle, now, max_cost, cost_per_byte)
        if err != 0:
            raise BadSpendBundleError(f"validation failure {err}")
        additions = spend_bundle.additions()
        removals = spend_bundle.removals()
        for new_coin in additions:
            self._add_coin_entry(new_coin, now)
        for spent_coin in removals:
            coin_name = spent_coin.name()
            coin_record = self._db[coin_name]
            self._db[coin_name] = replace(coin_record, spent_block_index=now.height)
        return additions, spend_bundle.coin_spends

    def coins_for_puzzle_hash(self, puzzle_hash: bytes32) -> Iterator[Coin]:
        for coin_name in self._ph_index[puzzle_hash]:
            coin_entry = self._db[coin_name]
            assert coin_entry.coin.puzzle_hash == puzzle_hash
            yield coin_entry.coin

    def all_coins(self) -> Iterator[Coin]:
        for coin_entry in self._db.values():
            yield coin_entry.coin

    def all_unspent_coins(self) -> Iterator[Coin]:
        for coin_entry in self._db.values():
            if not coin_entry.spent:
                yield coin_entry.coin

    def _add_coin_entry(self, coin: Coin, birthday: CoinTimestamp) -> None:
        name = coin.name()
        # assert name not in self._db
        self._db[name] = CoinRecord(
            coin,
            uint32(birthday.height),
            uint32(0),
            False,
            uint64(birthday.seconds),
        )
        self._ph_index[coin.puzzle_hash].append(name)

    def coin_record(self, coin_id: bytes32) -> Optional[CoinRecord]:
        return self._db.get(coin_id)
