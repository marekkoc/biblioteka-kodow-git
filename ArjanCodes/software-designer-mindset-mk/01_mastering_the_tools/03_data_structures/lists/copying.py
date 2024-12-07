from copy import copy, deepcopy


def main() -> None:
    numbers = [1, 2, 3, 4, 5]

    shallow_copied_list = copy(numbers)
    shallow_copied_list[0] = 20
    print("Original list after shallow copy modification:", numbers)
    print("Shallow copied list:", shallow_copied_list)

    mixed_list = [1, "Hello", 3.14]
    # Deep copy
    deep_copied_list = deepcopy(mixed_list)
    deep_copied_list[3] = 10
    print("Original list after deep copy modification:", mixed_list)
    print("Deep copied list:", deep_copied_list)


if __name__ == "__main__":
    main()
