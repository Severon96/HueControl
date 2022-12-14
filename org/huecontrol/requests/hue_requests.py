from requests import get, post, Response
from enum import Enum


class Request_Paths(Enum):
    API = "/api"


def post_request(path: str, payload) -> Response:
    return post(path, json=payload)


def get_request(path: str) -> Response:
    return get(path)
