def add_book(collection:list[dict], title:str, author:str):
    collection.append({"title": title, "author": author})


def display_books(collection:list[dict]):
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
    print()
    my_books = []
    add_book(my_books, "1984", "George Orwell")
    add_book(my_books, "To Kill a Mockingbird", "Harper Lee")
    add_book(my_books, "LinkedIn w praktyce", "Angelika Chimkowska")
    add_book(my_books, "Jedna rzecz", "Gary Keller")

    display_books(my_books)

    
    print(len(my_books))
    print(find_book_by_title(my_books, "1984"))


if __name__ == "__main__":
    main()
