def main() -> None:
    # Creating a dictionary with items added in a specific order
    ordered_dict = {"first": 1, "second": 2, "third": 3, "fourth": 4}

    # Adding an additional item to see it reflected at the end
    ordered_dict["fifth"] = 5

    # Iterating over the dictionary and printing items
    for key, value in ordered_dict.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
