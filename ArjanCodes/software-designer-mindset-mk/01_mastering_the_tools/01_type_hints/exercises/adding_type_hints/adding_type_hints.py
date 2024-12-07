def add_book(collection, title, author):
    collection.append({"title": title, "author": author})


def display_books(collection):
    for book in collection:
        print(f"Title: {book['title']}, Author: {book['author']}")


def find_book_by_title(collection, title):
    for book in collection:
        if book["title"] == title:
            return book
    return None


def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]


def main():
    my_books = []
    add_book(my_books, "1984", "George Orwell")
    add_book(my_books, "To Kill a Mockingbird", "Harper Lee")
    display_books(my_books)


if __name__ == "__main__":
    main()
