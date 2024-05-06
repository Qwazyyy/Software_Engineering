def heron_area(a, b, c):
    import math
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return area
