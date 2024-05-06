# Тема 8. Введение в ООП
Отчет по Теме #8 выполнил:
- Гребенщиков Евгений Олегович
- ИНО ОЗБ ПОАС-22-2

| Задание    | Сам_раб |
|------------|---------|
| Задание 1  | +       |
| Задание 2  | +       |
| Задание 3  | +       |
| Задание 4  | +       |
| Задание 5  | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
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

```
### Результат
![Lab8_1](./img/img.png)


## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

```
### Результат
![Lab8_2](./img/img_1.png)

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.


```python
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


class EBook(Book):
    def __init__(self, title, author, year, genre, file_format):
        super().__init__(title, author, year, genre)
        self.file_format = file_format

    def convert_to_format(self, new_format):
        print(f"Конвертация книги в {new_format} формат...")
        self.file_format = new_format
        print("Конвертация завершена.")

    def display_info(self):
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год: {self.year}")
        print(f"Жанр: {self.genre}")
        print(f"Формат: {self.file_format}")
        print()


# Создаем объект класса EBook с начальными характеристиками и форматом файла
ebook = EBook("Оно", "", 1925, "Ужасы", "PDF")

# Выводим информацию о электронной книге
ebook.display_info()

# Конвертируем книгу в другой формат
ebook.convert_to_format("EPUB")

ebook.display_info()

```
### Результат
![Lab8_3](./img/img_2.png)

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

```
### Результат
![Lab8_4](./img/img_3.png)


## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

```

### Результат
![Lab8_5](./img/img_4.png)