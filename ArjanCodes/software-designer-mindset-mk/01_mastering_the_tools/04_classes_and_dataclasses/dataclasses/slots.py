from dataclasses import dataclass, field
from typing import Self


@dataclass(slots=True)
class Point:
    x: int
    y: int
    neighbors: list[Self] = field(default_factory=list[Self])


def main() -> None:
    point = Point(10, 20, [Point(10, 20), Point(20, 30)])

    print(point)


if __name__ == "__main__":
    main()
