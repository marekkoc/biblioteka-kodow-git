CUSTOMERS = {
    "Alice": {"phone_number": "2341", "credit_card": "2341"},
    "Bob": {"phone_number": "9102", "credit_card": "5342"},
}


def update_phone_number(key: str, new_number: str) -> None:
    CUSTOMERS[key]["phone_number"] = new_number


def main() -> None:
    print(f"Before: {CUSTOMERS}")
    update_phone_number("Alice", "1234")
    print(f"After: {CUSTOMERS}")


if __name__ == "__main__":
    main()
