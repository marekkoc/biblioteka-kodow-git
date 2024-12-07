from typing import Protocol


# Third-party library 1
class FileLogger:
    def log_to_file(self, message: str) -> None:
        print(f"Logging to file: {message}")


# Third-party library 2
class ConsoleLogger:
    def console_log(self, message: str) -> None:
        print(f"Logging to console: {message}")


# Third-party library 3
class NetworkLogger:
    def send_log(self, message: str) -> None:
        print(f"Sending log over network: {message}")


class FileLoggerAdapter:
    def __init__(self, file_logger: FileLogger):
        self.file_logger = file_logger

    def log(self, message: str) -> None:
        self.file_logger.log_to_file(message)


class ConsoleLoggerAdapter:
    def __init__(self, console_logger: ConsoleLogger):
        self.console_logger = console_logger

    def log(self, message: str) -> None:
        self.console_logger.console_log(message)


class NetworkLoggerAdapter:
    def __init__(self, network_logger: NetworkLogger):
        self.network_logger = network_logger

    def log(self, message: str) -> None:
        self.network_logger.send_log(message)


# Our logger protocol
class LoggerProtocol(Protocol):
    def log(self, message: str) -> None: ...


def log_message(logger: LoggerProtocol, message: str) -> None:
    logger.log(message)


def main() -> None:
    file_logger = FileLoggerAdapter(FileLogger())
    console_logger = ConsoleLoggerAdapter(ConsoleLogger())
    network_logger = NetworkLoggerAdapter(NetworkLogger())

    # Now you can log messages through different loggers using the same function
    log_message(file_logger, "File logger example")
    log_message(console_logger, "Console logger example")
    log_message(network_logger, "Network logger example")


if __name__ == "__main__":
    main()
