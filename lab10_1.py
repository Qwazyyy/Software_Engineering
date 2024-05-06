import time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнена за : {end_time - start_time} секунд")
        return result

    return wrapper


@calculate_time
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2,200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end='')

    print("\n")


if __name__ == "__main__":
    result = fibonacci()
