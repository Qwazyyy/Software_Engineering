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


class PaperBook(Book):
    def __init__(self, title, author, year, genre, pages):
        super().__init__(title, author, year, genre)
        self.pages = pages

    def display_info(self):
        print("Бумажная книга информация:")
        print(f"Название: {self.get_title()}")
        print(f"Автор: {self.get_author()}")
        print(f"Год: {self.get_year()}")
        print(f"Жанр: {self.get_genre()}")
        print(f"Количество страниц: {self.pages}")
        print()


class EBook(Book):
    def __init__(self, title, author, year, genre, file_format):
        super().__init__(title, author, year, genre)
        self.file_format = file_format

    def display_info(self):
        print("Электронная книга - информация:")
        print(f"Название: {self.get_title()}")
        print(f"Автор: {self.get_author()}")
        print(f"Год: {self.get_year()}")
        print(f"Жанр: {self.get_genre()}")
        print(f"Формат файла: {self.file_format}")
        print()


# Создаем объекты классов PaperBook и EBook
paper_book = PaperBook("Оно", "Стивен Кинг", 1986, "Ужасы", 180)
ebook = EBook("Побег из Шоушенка", "Стивен Кинг", 1994, "Детектив", "PDF")

# Выводим информацию о книгах
paper_book.display_info()
ebook.display_info()
