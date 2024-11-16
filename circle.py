import math


def area(r):
    """
    Вычисляет площадь круга.

    Параметры:
    r (float): Радиус круга.

    Пример:
    >>> area(5)
    78.53981633974483
    """
    if r < 0:
        raise ValueError("Радиус должен быть неотрицательным")

    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет периметр круга.

    Параметры:
    r (float): Радиус круга.

    Пример:
    >>> perimeter(5)
    31.41592653589793
    """
    if r < 0:
        raise ValueError("Радиус должен быть неотрицательным")

    return 2 * math.pi * r
