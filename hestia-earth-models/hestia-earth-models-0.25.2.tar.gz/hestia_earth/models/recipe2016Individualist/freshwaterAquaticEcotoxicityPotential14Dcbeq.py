from hestia_earth.schema import IndicatorStatsDefinition, TermTermType

from hestia_earth.models.log import logRequirements, logShouldRun
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import convert_value_from_cycle, get_product
from hestia_earth.models.utils.cycle import impact_lookup_value as cycle_lookup_value
from hestia_earth.models.utils.input import sum_input_impacts
from . import MODEL

TERM_ID = 'freshwaterAquaticEcotoxicityPotential14Dcbeq'
LOOKUP_COLUMN = '14DCBeqIndividualistFreshwaterEcotoxicityReCiPe2016'


def _indicator(value: float):
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    indicator['statsDefinition'] = IndicatorStatsDefinition.MODELLED.value
    return indicator


def run(impact_assessment: dict):
    cycle = impact_assessment.get('cycle', {})
    product = get_product(impact_assessment)
    pesticides_value = convert_value_from_cycle(
        product, cycle_lookup_value(TERM_ID, cycle.get('inputs', []), TermTermType.PESTICIDEAI, LOOKUP_COLUMN), None
    )
    inputs_value = convert_value_from_cycle(product, sum_input_impacts(cycle.get('inputs', []), TERM_ID), None)
    logRequirements(model=MODEL, term=TERM_ID,
                    pesticides_value=pesticides_value,
                    inputs_value=inputs_value)
    logShouldRun(MODEL, TERM_ID, True)
    return _indicator(
        (pesticides_value or 0) + (inputs_value or 0)
    ) if any([pesticides_value, inputs_value]) else None
