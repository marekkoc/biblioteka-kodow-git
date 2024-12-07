def main() -> None:
    # Creating and manipulating a dictionary
    person: dict[str | int, str] = {
        "name": "Arjan",
        "profession": "Developer",
        "city": "Utrecht",
    }
    print("Original Dictionary:", person)

    # Dictionaries are mutable: values can be changed based on their keys
    person["name"] = "Jane"  # Changing the value associated with the key 'name'
    print(f"Dictionary after changing 'name': {person}")

    # Accessing elements using their keys
    profession = person["profession"]
    print(f"profession: {profession}")

    # Adding a new key-value pair
    person["profession"] = "YouTuber"
    print(f"Dictionary after adding a new key-value pair: {person}")

    # Removing a key-value pair
    del person["city"]
    print(f"Dictionary after removing 'city': {person}")

    # Keys and values can be of different types
    person[1] = "One"
    print("Mixed Type Dictionary:", person)

    # Discussing memory management
    # Python dictionaries automatically resize and rehash as items are added or removed
    person["hobby"] = "Photography"
    print(f"Dictionary after adding a new hobby: {person}")

    # Getting a list of all keys and values
    print(f"Keys: {person.keys()}")
    print(f"Values: {person.values()}")


if __name__ == "__main__":
    main()
