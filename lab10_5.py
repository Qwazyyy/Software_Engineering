class MyCustomException(Exception):
    def __init__(self):
        super().__init__("Деление на ноль невозможно")


def divide(a, b):
    if b == 0:
        raise MyCustomException()
    return a / b


def calculate_sum(numbers):
    try:
        sum = 0
        for num in numbers:
            sum += divide(num, 0)
    except MyCustomException as e:
        print(f"Произошла ошибка: {e}")
    else:
        print(f"Сумма чисел: {sum}")


def user_divide():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        result = divide(a, b)
    except MyCustomException as e:
        print(f"Произошла ошибка: {e}")
    else:
        print(f"Результат деления: {result}")


numbers = [1, 2, 3, 4, 5]
calculate_sum(numbers)
user_divide()
