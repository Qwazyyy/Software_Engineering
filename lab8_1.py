class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год: {self.year}")
        print()

# Создаем объекты класса Book
book = Book("Оно", "Стивен Кинг", 1966)

# Выводим информацию о каждой книге
book.display_info()
