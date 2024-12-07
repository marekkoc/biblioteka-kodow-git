from abc import ABC, abstractmethod


class IOPlugin(ABC):
    def __init__(self):
        self.path = None

    @abstractmethod
    def read(self, path: str):
        pass

    @abstractmethod
    def write(self, content: str):
        pass


class BarCodeReaderPlugin(IOPlugin):
    def __init__(self):
        super().__init__()

    def read(self, path: str):
        print("reading from", path)

    def write(self, content: str):
        print(f"writing content: {content} to BarCode reader: {self.path}")


class CDReaderPlugin(IOPlugin):
    def __init__(self):
        super().__init__()

    def read(self, path: str):
        print("reading  from", path)

    def write(self, content: str):
        print(f"writing content: {content} to CD reader: {self.path}")


def main() -> None:
    bar_code_reader = BarCodeReaderPlugin()
    cd_reader = CDReaderPlugin()
    bar_code_reader.read("path/to/bar_code")
    bar_code_reader.write("path/to/bar_code")
    cd_reader.read("path/to/file")
    cd_reader.write("path/to/file")


if __name__ == "__main__":
    main()
