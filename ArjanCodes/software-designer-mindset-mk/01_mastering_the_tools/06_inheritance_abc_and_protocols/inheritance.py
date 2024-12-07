from datetime import datetime


class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        raise NotImplementedError("Subclass must implement abstract method")

    def renew_license(self, new_license_date: datetime) -> str:
        raise NotImplementedError("Subclass must implement abstract method")


class Car(Vehicle):
    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Car reserved from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}."

    def renew_license(self, new_license_date: datetime) -> str:
        return f"Renewing license of truck {self.model} to {new_license_date}."


class Truck(Vehicle):
    def reserve(self, start_date: datetime, end_date: datetime) -> str:
        return f"Truck reserved from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}."

    def renew_license(self, new_license_date: datetime):
        return f"Renewing license of truck {self.model} to {new_license_date}."


def reserve_now(vehicle: Vehicle, start_date: datetime, end_date: datetime):
    print(f"Reserving a {vehicle.reserve(start_date, end_date)}")


def main() -> None:
    car = Car("Toyota", "Camry", 2020)
    truck = Truck("Ford", "F-150", 2019)
    reserve_now(car, datetime(2024, 1, 1), datetime(2024, 1, 7))
    reserve_now(truck, datetime(2024, 1, 1), datetime(2024, 1, 7))


if __name__ == "__main__":
    main()
