class Book:
    def __init__(self, title, author, year, genre):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__genre = genre

    def display_info(self):
        print(f"Название: {self.__title}")
        print(f"Автор: {self.__author}")
        print(f"Год: {self.__year}")
        print(f"Жанр: {self.__genre}")
        print()

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def set_genre(self, new_genre):
        self.__genre = new_genre
        print(f"Установка жанра: {self.__genre}")

# Создаем объект класса Book с начальными характеристиками книги
book = Book("Оно", "Стивен Кинг", 1966, "Ужасы")

# Получаем доступ к атрибутам книги через методы
print("Название:", book.get_title())
print("Автор:", book.get_author())
print("Год выпуска:", book.get_year())
print("Жанр:", book.get_genre())
