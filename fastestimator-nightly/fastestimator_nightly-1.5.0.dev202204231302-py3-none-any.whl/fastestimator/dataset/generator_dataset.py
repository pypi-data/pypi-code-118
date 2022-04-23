# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from typing import Any, Dict, Generator, Iterable, List, Optional, Sequence, Sized

from fastestimator.dataset.dataset import DatasetSummary, FEDataset, KeySummary
from fastestimator.util.traceability_util import traceable
from fastestimator.util.util import get_shape, get_type


@traceable(blacklist='_summary')
class GeneratorDataset(FEDataset):
    """A dataset from a generator function.

    Args:
        generator: The generator function to invoke in order to get a data sample.
        samples_per_epoch: How many samples should be drawn from the generator during an epoch. Note that the generator
            function will actually be invoke more times than the number specified here due to backend validation
            routines.
    """
    def __init__(self, generator: Generator[Dict[str, Any], int, None], samples_per_epoch: int) -> None:
        self.generator = generator
        self.samples_per_epoch = samples_per_epoch
        next(self.generator)  # Can't send non-none values to a new generator, so need to run a 'warm-up' first
        self._summary = None

    def __len__(self):
        return self.samples_per_epoch

    def __getitem__(self, index: int):
        return self.generator.send(index)

    def _do_split(self, splits: Sequence[Iterable[int]]) -> List['GeneratorDataset']:
        """Split the current dataset apart into several smaller datasets.

        Args:
            splits: Which indices to remove from the current dataset in order to create new dataset(s). One dataset will
                be generated for every iterable within the `splits` sequence.

        Returns:
            New datasets generated by removing data at the indices specified by `splits` from the current dataset.
        """
        print("FastEstimator-Warn: You probably don't actually want to split a generator dataset")
        self._summary = None
        results = []
        for split in splits:
            if isinstance(split, Sized):
                size = len(split)
            else:
                # TODO - make this efficient somehow
                size = sum(1 for _ in split)
            results.append(GeneratorDataset(self.generator, size))
            self.samples_per_epoch -= size
        return results

    def _get_stratified_splits(self, split_counts: List[int], seed: Optional[int],
                               stratify: str) -> Sequence[Iterable[int]]:
        print("\033[93m {}\033[00m".format(
            "Warning! GeneratorDataset does not support stratified splits. Falling back to classical split method."))
        return self._get_fractional_splits(split_counts=split_counts, seed=seed)

    def summary(self) -> DatasetSummary:
        """Generate a summary representation of this dataset.
        Returns:
            A summary representation of this dataset.
        """
        if self._summary is not None:
            return self._summary
        sample = self[0]
        key_summary = {}
        for key in sample.keys():
            val = sample[key]
            # TODO - if val is empty list, should find a sample which has entries
            shape = get_shape(val)
            dtype = get_type(val)
            key_summary[key] = KeySummary(num_unique_values=None, shape=shape, dtype=dtype)
        self._summary = DatasetSummary(num_instances=self.samples_per_epoch, keys=key_summary)
        return self._summary
