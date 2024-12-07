from enum import Enum


class HTTPStatus(Enum):
    OK = (200, "Request succeeded.")
    NOT_FOUND = (404, "Resource not found.")

    def __init__(self, code: int, description: str):
        self.code = code
        self.description = description


def action(status: HTTPStatus) -> str:
    match status:
        case HTTPStatus.OK:
            return "Request succeeded"
        case HTTPStatus.NOT_FOUND:
            return "Resource not found"


def main() -> None:
    status = HTTPStatus(200)

    print(action(status))
