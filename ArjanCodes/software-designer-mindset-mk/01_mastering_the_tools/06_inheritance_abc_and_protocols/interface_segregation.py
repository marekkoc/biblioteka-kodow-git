import math
from dataclasses import dataclass
from datetime import datetime
from typing import Protocol


class Rentable(Protocol):
    def reserve(self, start_date: datetime, days: int) -> None:
        """A vehicle can be reserved for renting."""
        ...


class Renewable(Protocol):
    def renew_license(self, new_license_date: datetime) -> None:
        """Renews the license of a vehicle."""
        ...

    def recall_license(self, date: datetime, garage: str) -> None:
        """Recalls the vehicle to the garage for license issues."""
        ...


class Maintainable(Protocol):
    def recall_for_maintenance(self, date: datetime, garage: str) -> None:
        """Recalls the vehicle to the garage for maintenance."""
        ...


@dataclass
class Car:
    model: str
    reserved: bool = False

    def reserve(self, start_date: datetime, days: int):
        self.reserved = True
        print(f"Reserving car {self.model} for {days} days at date {start_date}.")

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of car {self.model} to {new_license_date}.")

    def recall_license(self, date: datetime, garage: str):
        print(
            f"Recalling truck {self.model} to the garage {garage} at date {date} for license issues."
        )


@dataclass
class Truck:
    model: str
    reserved: bool = False
    reserved_trailer: bool = False

    def reserve(self, start_date: datetime, days: int):
        months = math.ceil(days / 30)
        self.reserved = True
        self.reserved_trailer = True
        print(
            f"Reserving truck {self.model} for {months} month(s) at date {start_date}, including a trailer."
        )

    def renew_license(self, new_license_date: datetime):
        print(f"Renewing license of truck {self.model} to {new_license_date}.")

    def recall_license(self, date: datetime, garage: str):
        print(
            f"Recalling truck {self.model} to the garage {garage} at date {date} for license issues."
        )


def reserve_now(vehicle: Rentable):
    vehicle.reserve(datetime.now(), 40)


def book_renewal(vehicle: Renewable):
    vehicle.renew_license(datetime.now())


def main() -> None:
    car = Car("Ford")
    truck = Truck("DAF")
    reserve_now(car)
    reserve_now(truck)

    book_renewal(car)


if __name__ == "__main__":
    main()
