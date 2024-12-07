from dataclasses import dataclass
from enum import StrEnum, auto


class FuelType(StrEnum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str
    driving_miles: int = 0
    fuel_type: FuelType = FuelType.ELECTRIC

    def needs_maintenance(self, maintenance_miles: int = 10000) -> bool:
        return self.driving_miles >= maintenance_miles


def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        license_plate="ABC-123",
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        license_plate="DEF-456",
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        license_plate="GHI-789",
        fuel_type=FuelType.PETROL,
    )

    print(tesla)
    print(volkswagen)
    print(bmw)


if __name__ == "__main__":
    main()
