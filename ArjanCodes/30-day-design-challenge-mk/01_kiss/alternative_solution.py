# This code was originally written by @erderial.


def count_fruits(fruits: list[str]) -> dict[str, int]:
    """Create an empty dictionary. Check if the item exists as a key using the *get* method. If not, create key with 0 as a default value, if it does just add 1 to the value."""
    d: dict[str, int] = {}
    for item in fruits:
        d[item] = d.get(item, 0) + 1
    return d


def main() -> None:
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}
    assert count_fruits([]) == {}
    assert count_fruits(["apple", "apple", "apple", "apple"]) == {"apple": 4}
    assert count_fruits(["banana"]) == {"banana": 1}


if __name__ == "__main__":
    main()
