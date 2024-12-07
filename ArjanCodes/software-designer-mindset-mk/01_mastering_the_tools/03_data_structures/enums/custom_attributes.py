from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def luminance(self):
        return 0.2126 * self.red + 0.7152 * self.green + 0.0722 * self.blue


class HTTPStatus(Enum):
    OK = (200, "Request succeeded.")
    NOT_FOUND = (404, "Resource not found.")

    def __init__(self, code: int, description: str):
        self.code = code
        self.description = description


def main() -> None:
    print(HTTPStatus.OK.description)


if __name__ == "__main__":
    main()
