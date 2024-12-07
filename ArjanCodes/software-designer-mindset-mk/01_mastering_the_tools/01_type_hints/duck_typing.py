my_str = "Hello World"
my_list = [34, 54, 65, 78]
my_dict = {"one": 123, "two": 456, "three": 789}

len(my_str)  # 11
len(my_list)  # 4
len(my_dict)  # 3


class Book:
    def __init__(self, author: str, title: str, pages: int):
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages


def output_book(book: Book):
    print(f"{book.title}, by {book.author}")


output_book(Book("Robert Martin", "Clean Code", 464))

print(len(Book("Robert Martin", "Clean Code", 464)))
