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
    return 2 * math.pi * r
