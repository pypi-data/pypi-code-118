import io
from typing import Optional

import pandas as pd

from algoralabs.common.requests import __post_request
from algoralabs.data_engine.utils import TransformOverride, Metrics, construct_metrics
from algoralabs.decorators.data import data_request


@data_request(transformer=lambda r: construct_metrics(r))
def analyze_data(data: pd.DataFrame) -> Metrics:
    endpoint = f"data-engine/alpha/analyze"

    parquet_bytes = data.to_parquet()
    return __post_request(endpoint, files={'file': parquet_bytes})


@data_request(process_response=lambda r: r.content, transformer=lambda r: pd.read_parquet(io.BytesIO(r)))
def transform_data(data: pd.DataFrame, transform_override: Optional[TransformOverride] = None) -> pd.DataFrame:
    endpoint = f"data-engine/alpha/transform"

    if transform_override is not None:
        transform_override = {'transform_override': transform_override.json()}
    else:
        transform_override = None

    parquet_bytes = data.to_parquet()
    return __post_request(endpoint, data=transform_override, files={'file': parquet_bytes})
