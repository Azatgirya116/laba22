BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]
class Book:
    def __init__(self, id, name, pages):

        if id < 0:
            raise ValueError("id должно быть положительным числом")
        if not isinstance(id, int):
            raise TypeError("id должно быть типа int")
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть типа str")
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        self.id = id
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_={self.id!r}, name={self.name!r}, pages={self.pages!r})'


class Library:
    def __init__(self, books=None):
        self.books = books
    def get_next_book_id(self) -> int:
        if self.books == None:
            return 1
        else:
            return len(self.books) + 1

    def get_index_by_book_id(self, book_id) -> int:
       for i, j in enumerate(self.books):
           if i + 1 == book_id:
               return i
       raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
   empty_library = Library()  # инициализируем пустую библиотеку
   print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

   list_books = [
       Book(id=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
]
   library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
   print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

   print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1