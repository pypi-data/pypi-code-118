import json

from algoralabs.common.requests import __delete_request, __post_request, __get_request, __put_request
from algoralabs.data.datasets.models import FieldRequest
from algoralabs.data.transformations.response_transformers import no_transform
from algoralabs.decorators.data import data_request


@data_request(transformer=no_transform)
def get_field(id: str):
    endpoint = f"data/datasets/field/{id}"
    return __get_request(endpoint)


@data_request(transformer=no_transform)
def create_field(request: FieldRequest):
    endpoint = f"data/datasets/field"
    return __put_request(endpoint, json=json.loads(request.json()))


@data_request(transformer=no_transform)
def update_field(id: str, request: FieldRequest):
    endpoint = f"data/datasets/field/{id}"
    return __post_request(endpoint, json=json.loads(request.json()))


@data_request(transformer=no_transform)
def delete_field(id: str) -> None:
    endpoint = f"data/datasets/field/{id}"
    return __delete_request(endpoint)
