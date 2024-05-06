import math


def heron_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

max_a = max(one)
max_b = max(two)
max_c = max(three)

min_a = min(one)
min_b = min(two)
min_c = min(three)

area_max = heron_area(max_a, max_b, max_c)
area_min = heron_area(min_a, min_b, min_c)

print("Площадь треугольника из максимальных сторон:", area_max)
print("Площадь треугольника из минимальных сторон:", area_min)
