from hestia_earth.schema import EmissionMethodTier, EmissionStatsDefinition

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.constant import Units, get_atomic_conversion
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.input import total_excreta_n
from hestia_earth.models.utils.excretaManagement import get_lookup_factor
from . import MODEL

TERM_ID = 'no3ToGroundwaterExcreta'
TIER = EmissionMethodTier.TIER_2.value


def _emission(value: float):
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = TIER
    emission['statsDefinition'] = EmissionStatsDefinition.MODELLED.value
    return emission


def _run(excretaKgN: float, NO3_N_EF: float):
    value = NO3_N_EF * excretaKgN * get_atomic_conversion(Units.KG_NO3, Units.TO_N)
    return [_emission(value)]


def _should_run(cycle: dict):
    excretaKgN = total_excreta_n(cycle.get('inputs', []))
    NO3_N_EF = get_lookup_factor(cycle.get('practices', []), 'EF_NO3-N')

    logRequirements(model=MODEL, term=TERM_ID,
                    excretaKgN=excretaKgN,
                    NO3_N_EF=NO3_N_EF)

    should_run = all([excretaKgN, NO3_N_EF])
    logShouldRun(MODEL, TERM_ID, should_run, methodTier=TIER)
    return should_run, excretaKgN, NO3_N_EF


def run(cycle: dict):
    should_run, excretaKgN, NO3_N_EF = _should_run(cycle)
    return _run(excretaKgN, NO3_N_EF) if should_run else []
