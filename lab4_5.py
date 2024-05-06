# Lab4_5.py
from triangle_area import heron_area


def get_triangle_sides():
    """Получение сторон треугольника от пользователя."""
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    return a, b, c


def main():
    print("Программа для вычисления площади треугольника по формуле Герона.")
    a, b, c = get_triangle_sides()
    area = heron_area(a, b, c)
    print(f"Площадь треугольника: {area:.2f} квадратных единиц")


if __name__ == "__main__":
    main()
