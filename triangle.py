def area(a, h):
    """
    Вычисляет площадь треугольника.

    Параметры:
    a (float): Основание треугольника.
    h (float): Высота треугольника.

    Пример:
    >>> area(4, 5)
    10.0
    """
    if any(param < 0 for param in (a, h)):
        raise ValueError("Длины должны быть неотрицательными")

    return a * h / 2


def perimeter(a, b, c):
    """
    Вычисляет периметр треугольника.

    Параметры:
    a, b, c (float): Длины сторон треугольника.

    Пример:
    >>> perimeter(3, 4, 5)
    12
    """
    if any(param < 0 for param in (a, b, c)):
        raise ValueError("Длины должны быть неотрицательными")

    return a + b + c
