def main() -> None:
    sum = 0.1 + 0.1 + 0.1
    expected = 0.3

    print(f"sum = {sum}, expected = {expected}")
    assert sum == expected


if __name__ == "__main__":
    main()
