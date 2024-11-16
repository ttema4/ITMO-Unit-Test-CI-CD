def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
    a (float): Длина.
    b (float): Ширина.

    Пример:
    >>> area(4, 5)
    20
    """
    if any(param < 0 for param in (a, b)):
        raise ValueError("Длины должны быть неотрицательными")

    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
    a (float): Длина.
    b (float): Ширина.

    Пример:
    >>> perimeter(4, 5)
    18
    """
    if any(param < 0 for param in (a, b)):
        raise ValueError("Длины должны быть неотрицательными")

    return 2 * (a + b)
