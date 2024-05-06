# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме #6 выполнил:
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
### При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные вам форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте вашу задумку. Для получения начальных данных используйте input(). Результатом программы будет выведенный список и кортеж из начальных данных

```python
user_input = input("Введите числа, разделенные пробелом: ")
numbers_list = user_input.split()
numbers_tuple = tuple(numbers_list)
print("Список:", numbers_list)
print("Кортеж:", numbers_tuple)
```
### Результат
![Lab6_1](./img/img.png)

## Самостоятельная работа №2
### Николай знает, что кортежи являются неизменяемыми, но он очень упрямый и всегда хочет доказать, что он прав. Студент решил создать функцию, которая будет удалять первое появление определенного элемента из кортежа по значению и возвращать кортеж без него. Попробуйте повторить шедевр не признающего авторитеты начинающего программиста. Но учтите, что Николай не всегда уверен в наличии элемента в кортеже (в этом случае кортеж вернется функцией в исходном виде).
### Входные данные:
### (1, 2, 3), 1)
### (1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)
### (2, 4, 6, 6, 4, 2), 9)
### Ожидаемый результат:
### (2, 3)
### (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2)
### (2, 4, 6, 6, 4, 2)

```python
def remove_first_occurrence(tup, value):
    if value in tup:
        index = tup.index(value)
        return tup[:index] + tup[index + 1:]
    return tup


print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
```
### Результат
![Lab6_2](./img/img_1.png)

## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать победителя. Вам им нужно в этом помочь. Дана строка в виде случайной последовательности чисел от 0 до 9 (длина строки минимум 15 символов). Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте Михаил А. Панов функцию, принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел, также эти значения нужно вывести в порядке возрастания ключа.

```python
def most_frequent_digits(input_string):
    digit_count = {}

    for char in input_string:
        digit = int(char)
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1

    top_three_digits = sorted(digit_count.items(), key=lambda item: (-item[1], item[0]))[:3]

    result = {key: value for key, value in sorted(top_three_digits)}

    return result


input_string = input("Введите число: ")
output = most_frequent_digits(input_string)
print(output)
```
### Результат
![Lab6_3](./img/img_2.png)

## Самостоятельная работа №4
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
### Входные данные:
### (1, 2, 3), 8)
### (1, 8, 3, 4, 8, 8, 9, 2), 8)
### (1, 2, 8, 5, 1, 2, 9), 8)
### Ожидаемый результат:
### ()
### (8, 3, 4, 8)
### (8, 5, 1, 2, 9)

```python
def find_id_sequence(entries, search_id):
    try:
        first_index = entries.index(search_id)
    except ValueError:
        return ()

    try:
        second_index = entries.index(search_id, first_index + 1)
        return entries[first_index:second_index + 1]
    except ValueError:
        return entries[first_index:]


print(find_id_sequence((1, 2, 3), 8))
print(find_id_sequence((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(find_id_sequence((1, 2, 8, 5, 1, 2, 9), 8))
```
### Результат
![Lab6_4](./img/img_3.png)


## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, в которой будут обязательно использоваться кортеж или список. Проведите минимум три теста для проверки работоспособности вашей задачи.
### Функция должна возвращать список студентов, отсортированный по сумме баллов, начиная с самого успешного студента.
### Пример:
### Главный список: 
```python
students = [
    {"name": "Alice", "exam_score": 90, "homework_score": 85},
    {"name": "Bob", "exam_score": 80, "homework_score": 90},
    {"name": "Charlie", "exam_score": 90, "homework_score": 80},
]
```
### Ответ:
[{'name': 'Alice', 'exam_score': 90, 'homework_score': 85}, {'name': 'Bob', 'exam_score': 80, 'homework_score': 90}, {'name': 'Charlie', 'exam_score': 90, 'homework_score': 80}]
### Функция должна возвращать список студентов, отсортированный по сумме баллов, начиная с самого успешного студента

```python
def sort_students_by_total_score(students):
    sorted_students = sorted(students, key=lambda student: -(student["exam_score"] + student["homework_score"]))
    return sorted_students


students = [
    {"name": "Alice", "exam_score": 90, "homework_score": 85},
    {"name": "Bob", "exam_score": 80, "homework_score": 90},
    {"name": "Charlie", "exam_score": 90, "homework_score": 80},
]

sorted_students = sort_students_by_total_score(students)
print(sorted_students)

empty_students = []
sorted_empty_students = sort_students_by_total_score(empty_students)
print(sorted_empty_students)

single_student = [{"name": "Eve", "exam_score": 100, "homework_score": 95}]
sorted_single_student = sort_students_by_total_score(single_student)
print(sorted_single_student)
```

### Результат
![Lab6_5](./img/img_4.png)