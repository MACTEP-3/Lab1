# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Point:
    def __init__(self, x: float, y: float):
        """
        Создание и подготовка объекта "Точка"

        :param x: Значение координаты x в прямоугольной системе координат на плоскости
        :param y: Значение координаты y в прямоугольной системе координат на плоскости

        Примеры:
        >>> point = Point(3, 4)  # инициализация экземпляра класса
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Значение координаты x должно быть типа int или типа float")
        self.x = x

        if not isinstance(y, (int, float)):
            raise TypeError("Значение координаты y должно быть типа int или типа float")
        self.y = y

    def calculate_distance_to_origin(self) -> float:
        """
        Функция которая вычисляет расстояние от данной точки до начала системы координат

        :return: расстояние от данной точки до начала системы координат

        Примеры:
        >>> point = Point(3, 4)
        >>> point.calculate_distance_to_origin()
        """
        ...

    def shift_x(self, x: float) -> None:
        """
        Функция смещает координату x на заданное число (прибавляет переданное значение к x)

        :param x: Значение смещения координаты x

        :raise TypeError: Если переданное значение имеет тип не int и не float

        Примеры:
        >>> point = Point(3, 4)
        >>> point.shift_x(4)
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Значение смещения координаты должно быть типа int или типа float")
        ...

    def shift_y(self, y: float) -> None:
        """
        Функция смещает координату y на заданное число (прибавляет переданное значение к y)

        :param y: Значение смещения координаты y

        :raise TypeError: Если переданное значение имеет тип не int и не float

        Примеры:
        >>> point = Point(3, 4)
        >>> point.shift_y(4)
        """
        if not isinstance(y, (int, float)):
            raise TypeError("Значение смещения координаты должно быть типа int или типа float")
        ...

class Segment:
    def __init__(self, a: Point, b: Point):
        """
        Создание и подготовка объекта "Отрезок"

        :param a: Значение координат точки a (условного начала отрезка) в прямоугольной системе координат на плоскости
        :param b: Значение координат точки b (условного конца отрезка) в прямоугольной системе координат на плоскости

        Примеры:
        >>> segment = Segment(Point(3,4), Point(2,5))  # инициализация экземпляра класса
        """
        if not isinstance(a, Point):
            raise TypeError("Значение координаты точки a должно быть типа Point")
        self.a = a

        if not isinstance(b, Point):
            raise TypeError("Значение координаты точки b должно быть типа Point")
        self.b = b

    def calculate_length(self) -> float:
        """
        Функция вычисляет длину данного отрезка

        :return: Длина данного отрезка

        Примеры:
        >>> segment = Segment(Point(3,4), Point(2,5))
        >>> segment.calculate_length()
        1.4142135623730951
        """
        return ((self.b.x - self.a.x) ** 2 + (self.b.y - self.a.y) ** 2) ** (1/2) # Необходимо добавить релизацию, иначе возникнет ошибка в RightTriangle

    def is_point_in_segment(self, a: Point) -> bool:
        """
        Функция проверяет находится ли переданная точка на данном отрезке

        :return: Приналежит ли точка отрезку

        :raise TypeValue: Если переданный аргумент не является точкой типа Point

        Примеры:
        >>> segment = Segment(Point(0,0), Point(4,4))
        >>> segment.is_point_in_segment(Point(2,2))
        """
        if not isinstance(a, Point):
            raise TypeError("Значение точки должно быть типа Point")
        ...

class RightTriangle:
    def __init__(self, catheter_first: Segment, catheter_second: Segment, hypotenuse: Segment):
        """
        Создание и подготовка объекта "Прямоуголльный треугольник"

        :param catheter_first: Отрезок - один катет прямоугольного треугольника
        :param catheter_second: Отрезок - второй катет прямоугольного треугольника
        :param hypotenuse: Отрезок - гипотенуза прямоугольного треугольника

        Примеры:
        >>> righttriangle = RightTriangle(Segment(Point(0,3), Point(0,0)), Segment(Point(0,0), Point(4,0)), Segment(Point(0,3), Point(4,0)))
        """
        if not isinstance(catheter_first, Segment):
            raise TypeError("Катет должен быть типа Segment")

        if not isinstance(catheter_second, Segment):
            raise TypeError("Катет должен быть типа Segment")

        if not isinstance(hypotenuse, Segment):
            raise TypeError("Гипотенуза должна быть типа Segment")

        if catheter_first.calculate_length() ** 2 + catheter_second.calculate_length() ** 2 != hypotenuse.calculate_length() ** 2:
            raise ValueError("Треугольник с данными длинами сторон не является прямоугольным")
        self.cathether_first = catheter_first
        self.cathether_second = catheter_second
        self.hypotenuse = hypotenuse

    def sin_first(self) -> float:
        """
        Функция вычисляет значение синуса угла между первым катетом и гипотенузой

        :return: Значение синуса угла между первым катетом и гипотенузой

        Примеры:
        >>> righttriangle = RightTriangle(Segment(Point(0,3), Point(0,0)), Segment(Point(0,0), Point(4,0)), Segment(Point(0,3), Point(4,0)))
        >>> righttriangle.sin_first()
        """
        ...

    def cos_first(self) -> float:
        """
        Функция вычисляет значение косинуса угла между первым катетом и гипотенузой

        :return: Значение косинуса угла между первым катетом и гипотенузой

        Примеры:
        >>> righttriangle = RightTriangle(Segment(Point(0,3), Point(0,0)), Segment(Point(0,0), Point(4,0)), Segment(Point(0,3), Point(4,0)))
        >>> righttriangle.cos_first()
        """
        ...





if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
