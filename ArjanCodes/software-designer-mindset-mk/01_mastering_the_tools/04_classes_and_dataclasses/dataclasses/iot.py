from dataclasses import dataclass, field
from enum import StrEnum, auto


class ConnectivityStatus(StrEnum):
    ONLINE = auto()
    OFFLINE = auto()
    LIMITED = "Limited Connectivity"


@dataclass
class IoTDevice:
    name: str
    device_type: str
    connectivity: ConnectivityStatus
    sensors: list[str] = field(default_factory=list)
    location: str = "Unknown"
    firmware_version: int = 1

    def add_sensor(self, sensor_name: str):
        """Add a new sensor to the device."""
        self.sensors.append(sensor_name)

    def update_firmware(self, new_version: int):
        """Update the device's firmware version."""
        if new_version > self.firmware_version:
            self.firmware_version = new_version
            print(f"Firmware updated to version {new_version}.")
        else:
            print("Firmware is already up to date.")


def main() -> None:
    # Example usage
    iot_device = IoTDevice(
        name="Smart Thermostat",
        device_type="Thermostat",
        connectivity=ConnectivityStatus.ONLINE,
        location="Living Room",
    )
    iot_device.add_sensor("Temperature")


if __name__ == "__main__":
    main()
