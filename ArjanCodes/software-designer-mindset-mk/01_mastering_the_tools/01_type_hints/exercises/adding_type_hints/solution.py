def add_book(collection: list[dict[str, str]], title: str, author: str) -> None:
    collection.append({"title": title, "author": author})


def display_books(collection: list[dict[str, str]]) -> None:
    for book in collection:
        print(f"Title: {book['title']}, Author: {book['author']}")


def find_book_by_title(
    collection: list[dict[str, str]], title: str
) -> dict[str, str] | None:
    for book in collection:
        if book["title"] == title:
            return book
    return None


def filter_even_numbers(numbers: list[int]) -> list[int]:
    return [num for num in numbers if num % 2 == 0]


def main() -> None:
    my_books: list[dict[str, str]] = []
    add_book(my_books, "1984", "George Orwell")
    add_book(my_books, "To Kill a Mockingbird", "Harper Lee")
    display_books(my_books)


if __name__ == "__main__":
    main()
