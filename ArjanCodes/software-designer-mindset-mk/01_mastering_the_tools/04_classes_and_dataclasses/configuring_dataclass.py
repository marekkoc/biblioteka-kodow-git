from dataclasses import dataclass


# Equivalent class using dataclass
@dataclass(order=True)
class PersonDataclass:
    name: str
    age: int


# Class without dataclass
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __eq__(self, other: object):
        if not isinstance(other, Person):
            return False

        return self.name == other.name and self.age == other.age

    def __ne__(self, other: object):
        if not isinstance(other, Person):
            return False
        return not self.__eq__(other)

    def __lt__(self, other: "Person"):
        return self.age < other.age

    def __le__(self, other: "Person"):
        return self.age <= other.age

    def __gt__(self, other: "Person"):
        return self.age > other.age

    def __ge__(self, other: "Person"):
        return self.age >= other.age


def main() -> None:
    # Create instances of both classes
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

    person_dataclass1 = PersonDataclass("Alice", 30)
    person_dataclass2 = PersonDataclass("Bob", 25)

    # Check if instances are equal
    print(person1 == person2)  # Output: False
    print(person_dataclass1 == person_dataclass2)  # Output: False

    print(person1 != person2)  # Output: True
    print(person_dataclass1 != person_dataclass2)  # Output: True

    # Compare instances based on age
    print(person1 < person2)  # Output: False
    print(person_dataclass1 < person_dataclass2)  # Output: False

    print(person1 <= person2)  # Output: False
    print(person_dataclass1 <= person_dataclass2)  # Output: False

    print(person1 > person2)  # Output: True
    print(person_dataclass1 > person_dataclass2)  # Output: True

    print(person1 >= person2)  # Output: True
    print(person_dataclass1 >= person_dataclass2)  # Output: True

    # String representation of instances
    print(repr(person1))  # Output: Person(name=Alice, age=30)
    print(repr(person_dataclass1))  # Output: PersonDataclass(name='Alice', age=30)


if __name__ == "__main__":
    main()
