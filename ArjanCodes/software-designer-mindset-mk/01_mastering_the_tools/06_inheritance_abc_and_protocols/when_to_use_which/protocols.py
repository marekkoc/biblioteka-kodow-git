from typing import Protocol, Sequence


class MessageSource(Protocol):
    def read_message(self) -> str:
        """Read and return a message from the source."""
        ...


class FileMessageSource:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_message(self) -> str:
        # Logic to read and return a message from a file
        return "Message from file"


class NetworkMessageSource:
    def __init__(self, address: str):
        self.address = address

    def read_message(self) -> str:
        # Logic to read and return a message from a network socket
        return "Message from network"


class APIMessageSource:
    def __init__(self, api_url: str):
        self.api_url = api_url

    def read_message(self) -> str:
        # Logic to read and return a message from an API
        return "Message from API"


def process_messages(sources: Sequence[MessageSource]) -> None:
    for source in sources:
        message = source.read_message()
        print(f"Processing message: {message}")


def main() -> None:
    sources = [
        FileMessageSource("/path/to/file"),
        NetworkMessageSource("192.168.1.1"),
        APIMessageSource("https://api.example.com"),
    ]
    process_messages(sources)


if __name__ == "__main__":
    main()
