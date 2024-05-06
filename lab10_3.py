def add_two(user_input):
    try:
        result = 2 + int(user_input)
        print(f"Введенное число + 2: {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")


add_two(input("Введите число: "))
add_two(input("Введите число: "))
add_two(input("Введите число: "))
