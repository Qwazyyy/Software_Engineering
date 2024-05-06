class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год: {self.year}")
        print(f"Жанр: {self.genre}")
        print()

    def change_genre(self, new_genre):
        self.genre = new_genre
        print(f"Изменить жанр для: {self.genre}")

# Создаем объект класса Book
book = Book("Оно", "Стивен Кинг", 1966, "Ужасы")

# Выводим информацию о книге до изменения жанра
print("Информация о книге до изменения жанра:")
book.display_info()

# Изменяем жанр книги
book.change_genre("Классика")

# Выводим информацию о книге после изменения жанра
print("Информация о книге после изменения жанра:")
book.display_info()
