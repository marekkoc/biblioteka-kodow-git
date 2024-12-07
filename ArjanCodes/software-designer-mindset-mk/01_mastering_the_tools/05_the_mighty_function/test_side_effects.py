from side_effects import update_phone_number

CUSTOMERS = {
    "Alice": {"phone_number": "2341", "credit_card": "2341"},
    "Bob": {"phone_number": "9102", "credit_card": "5342"},
}


def test_update_phone_number():
    # Test case 1: Update phone number for existing customer
    customer_name = "Alice"
    new_phone_number = "9999"
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_non_existing_customer():
    # Test case 2: Update phone number for non-existing customer
    customer_name = "John"
    new_phone_number = "1234"
    update_phone_number(customer_name, new_phone_number)
    assert customer_name in CUSTOMERS
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_empty_string():
    # Test case 3: Update phone number with empty string
    customer_name = "Bob"
    new_phone_number = ""
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_special_characters():
    # Test case 4: Update phone number with special characters
    customer_name = "Alice"
    new_phone_number = "!@#$%"
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_long_string():
    # Test case 6: Update phone number with long string
    customer_name = "Alice"
    new_phone_number = "1234567890" * 10
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_leading_trailing_spaces():
    # Test case 7: Update phone number with leading/trailing spaces
    customer_name = "Bob"
    new_phone_number = "  1234  "
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number.strip()


def test_update_phone_number_numeric_string():
    # Test case 8: Update phone number with numeric string
    customer_name = "Alice"
    new_phone_number = "1234567890"
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_alphanumeric_string():
    # Test case 9: Update phone number with alphanumeric string
    customer_name = "Bob"
    new_phone_number = "abc123"
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number


def test_update_phone_number_special_characters_spaces():
    # Test case 10: Update phone number with special characters and spaces
    customer_name = "Alice"
    new_phone_number = "!@#$%  "
    update_phone_number(customer_name, new_phone_number)
    assert CUSTOMERS[customer_name]["phone_number"] == new_phone_number.strip()
