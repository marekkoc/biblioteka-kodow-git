def main() -> None:
    # True acts as 1, False acts as 0
    result = True + True  # Equals 2
    zero = True * False  # Equals 0

    print(f"result: {result}, zero: {zero}")
    print(f"zero: {zero}")

    options = ["False option", "True option"]
    choice = options[True]  # Selects 'True option'

    print(f"choice: {choice}")

    denominator = 0
    numerator = 10
    safe_division = denominator and numerator / denominator

    print(f"safe_division: {safe_division}")

    number = 10
    result = "Positive" if number >= 0 else "Negative"

    NOT = not True  # False
    AND = True and False  # False
    OR = True or False  # True

    print(f"NOT: {NOT}, AND: {AND}, OR: {OR}")

    truthy_count = sum([True, False, True, 1 == 1, False])  # 3

    print(f"truthy_count: {truthy_count}")

    x = 5
    is_valid_range = 1 <= x <= 10
    print(f"is_valid_range: {is_valid_range}")


if __name__ == "__main__":
    main()
