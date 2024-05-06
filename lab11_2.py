def fib(n):
    a, b = 1, 1
    with open('every_number.txt', 'w') as file:
        for _ in range(n):
            file.write(f"{a}\n")
            yield a
            a, b = b, a + b

print("Число Фибоначчи для 200: ", list(fib(200))[-1])