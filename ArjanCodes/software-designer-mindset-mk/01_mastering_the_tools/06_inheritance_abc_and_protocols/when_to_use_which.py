from abc import ABC, abstractmethod
from typing import Protocol


### ABCs
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: dict[str, str]) -> str:
        """Process the given data and return the result."""
        ...


class CSVProcessor(DataProcessor):
    def process(self, data: dict[str, str]) -> str:
        # Implement CSV-specific processing
        return f"CSV-processed {data}"


class JSONProcessor(DataProcessor):
    def process(self, data: dict[str, str]) -> str:
        # Implement JSON-specific processing
        return f"JSON-processed {data}"


### Protocols
class DataProcessorProtocol(Protocol):
    def process(self, data: dict[str, str]) -> str: ...


class XMLProcessor:
    def process(self, data: dict[str, str]) -> str:
        return f"XML-processed {data}"


class XLSXProcessor:
    def process(self, data: dict[str, str]) -> str:
        return f"JSON-processed {data}"


def main() -> None:
    csv_processor = CSVProcessor()
    json_processor = JSONProcessor()
    print(csv_processor.process({"name": "John", "age": "30"}))
    print(json_processor.process({"name": "John", "age": "30"}))

    xml_processor = XMLProcessor()
    xlsx_processor = XLSXProcessor()
    print(xml_processor.process({"name": "John", "age": "30"}))
    print(xlsx_processor.process({"name": "John", "age": "30"}))


if __name__ == "__main__":
    main()
