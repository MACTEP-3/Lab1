from enum import Enum
import doctest


class TypeOfTransport(Enum):
    car = "автомобильный"
    air = "воздушный"
    water = "водный"
    railway = "железнодорожный"


class Transport:
    def __init__(self, name: str, type_of_transport: TypeOfTransport):
        """
        Создание и подготовка объекта "Транспорт"
        Родительский класс, определяющий общие свойства и методы для всех видов транспорта.

        :param name: Имя транспорта. Имя транспорта после создания экземпляра изменить нельзя, оно отражает его строгую
        принадлежность к определённому классу, серии.
        :param type_of_transport: Тип транспорта типа TypeOfTransport. Тип транспорта после создания экземпляра изменить
         нельзя из физических соображений

        Примеры:
        >>> transport = Transport("Boeing 737 Original", TypeOfTransport.air)  # инициализация экземпляра класса
        """
        self._name = name
        if not isinstance(type_of_transport, TypeOfTransport):
            raise TypeError("Вид транспорта должен быть типа TypeOfTransport")
        self._type_of_transport = type_of_transport

    @property
    def name(self):
        """
        Получает значение свойства 'name'.

        :return: Значение свойства 'name'.
        """
        return self._name

    @property
    def type_of_transport(self):
        """
        Получает значение свойства 'type_of_transport'.

        :return: Значение свойства 'type_of_transport'.
        """
        return self._type_of_transport

    def __str__(self):
        """
        Возвращает строковое представление объекта "Транспорт".

        :return: Строковое представление объекта "Транспорт".
        """
        return f"Транспортное средство {self._name}. Вид транспорта {self._type_of_transport.value}"

    def __repr__(self):
        """
        Возвращает представление объекта "Транспорт" в виде строки, которое можно использовать для воссоздания объекта.

        :return: Представление объекта "Транспорт" в виде строки.
        """
        return f"{self.__class__.__name__}(name={self._name!r}, type_of_transport={self._type_of_transport.value!r})"


class CombustionEngineTransport(Transport):
    def __init__(self, name: str, type_of_transport: TypeOfTransport, engine_power: int, tank_volume: float,
                 fuel_volume: float):
        """
        Создание и подготовка объекта "Транспорт с ДВС" потомок
        Класс-потомок, представляющий вид транспорта с двигателем внутреннего сгорания

        :param name: Имя транспорта. Имя транспорта после создания экземпляра изменить нельзя, оно отражает его строгую
        принадлежность к определённому классу, серии.
        :param type_of_transport: Тип транспорта типа TypeOfTransport. Тип транспорта после создания экземпляра изменить
         нельзя из физических соображений
        :param engine_power: Значение мощности ДВС в л. с.
        :param tank_volume: Значение вместимости топливного бака в литрах
        :param fuel_volume: Значение количества литров топлива в топливком баке

        Примеры:
        >>> transport = CombustionEngineTransport("Ford Model AA", TypeOfTransport.car, 40, 64.0, 0.0)  # инициализация экземпляра класса
        """
        super().__init__(name, type_of_transport)  # Вызываем __init__() родительского класса
        if not isinstance(engine_power, int):
            raise TypeError("Мощность двигателя должна быть типа int")
        if engine_power <= 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self._engine_power = engine_power  # Добавляем дополнительное поле
        if not isinstance(tank_volume, float):
            raise TypeError("Вместимость бака должна быть типа float")
        if tank_volume <= 0:
            raise ValueError("Вместимость бака должна быть положительным числом")
        self._tank_volume = tank_volume  # Добавляем дополнительное поле
        if not isinstance(fuel_volume, float):
            raise TypeError("Количество литров топлива должно быть типа float")
        if fuel_volume < 0:
            raise ValueError("Количество литров топлива должно быть неотрицательным числом")
        if fuel_volume > self._tank_volume:
            raise ValueError("Количество литров топлива не может быть больше вместимости бака")
        self._fuel_volume = fuel_volume  # Добавляем дополнительное поле

    @property
    def engine_power(self):
        """
        Получает значение свойства 'engine_power'.

        :return: Значение свойства 'engine_power'.
        """
        return self._engine_power

    @engine_power.setter
    def engine_power(self, engine_power):
        """
        Устанавливает значение свойства 'engine_power'.

        :param engine_power: Новое значение свойства 'engine_power'.
        :raise TypeError: Если переданное значение имеет тип не int.
        :raise ValueError: Если переданное значение неположительное.
        """
        if not isinstance(engine_power, int):
            raise TypeError("Мощность двигателя должна быть типа int")
        if engine_power <= 0:
            raise ValueError("Мощность двигателя должна быть положительным числом")
        self._engine_power = engine_power

    @property
    def tank_volume(self):
        """
        Получает значение свойства 'tank_volume'.

        :return: Значение свойства 'tank_volume'.
        """
        return self._tank_volume

    @tank_volume.setter
    def tank_volume(self, tank_volume):
        """
        Устанавливает значение свойства 'tank_volume'.

        :param tank_volume: Новое значение свойства 'tank_volume'.
        :raise TypeError: Если переданное значение имеет тип не float.
        :raise ValueError: Если переданное значение неположительное.
        :raise ValueError: Если переданное значение меньше уже имеющегося количества литров топлива.
        """
        if not isinstance(tank_volume, float):
            raise TypeError("Вместимость бака должна быть типа float")
        if tank_volume <= 0:
            raise ValueError("Вместимость бака должна быть положительным числом")
        if tank_volume < self._fuel_volume:
            raise ValueError("Вместимость бака не может быть меньше уже имеющегося количества литров топлива")
        self._tank_volume = tank_volume

    @property
    def fuel_volume(self):
        """
        Получает значение свойства 'fuel_volume'.

        :return: Значение свойства 'fuel_volume'.
        """
        return self._fuel_volume

    def fill_up_the_tank(self, fuel_volume: float) -> float:
        """
        Функция которая заправляет бак на указанное количество литров

        :return: итоговое количество литров в баке

        :raise TypeError: Если переданное значение имеет тип не float.
        :raise ValueError: Если переданное значение неотрицательным.
        :raise ValueError: Если итоговое количество литров топлива больше вместимости бака.

        Примеры:
        >>> transport = CombustionEngineTransport("Ford Model AA", TypeOfTransport.car, 40, 64.0, 5.0)
        >>> transport.fill_up_the_tank(20.0)
        25.0
        """
        if not isinstance(fuel_volume, float):
            raise TypeError("Количество литров топлива должно быть типа float")
        if fuel_volume < 0:
            raise ValueError("Количество литров топлива должно быть неотрицательным числом")
        if fuel_volume + self._fuel_volume > self._tank_volume:
            raise ValueError(f"Итоговое количество литров топлива не может быть больше вместимости бака. "
                             f"Избыток {fuel_volume + self._fuel_volume - self._tank_volume}")
        self._fuel_volume += fuel_volume
        return self._fuel_volume

    def empty_the_tank(self, fuel_volume: float) -> float:
        """
        Функция которая опустошает бак на указанное количество литров

        :return: итоговое количество литров в баке

        :raise TypeError: Если переданное значение имеет тип не float.
        :raise ValueError: Если переданное значение неположительное.
        :raise ValueError: Если количество литров топлива меньше переданного значения.

        Примеры:
        >>> transport = CombustionEngineTransport("Ford Model AA", TypeOfTransport.car, 40, 64.0, 25.0)
        >>> transport.empty_the_tank(20.0)
        5.0
        """
        if not isinstance(fuel_volume, float):
            raise TypeError("Количество литров топлива должно быть типа float")
        if fuel_volume < 0:
            raise ValueError("Количество литров топлива должно быть неотрицательным числом")
        if fuel_volume > self._fuel_volume:
            raise ValueError(f"Невозможно слить больше имеющегося количества литров топлива. "
                             f"Недостаток {fuel_volume - self._fuel_volume}")
        self._fuel_volume -= fuel_volume
        return self._fuel_volume

    def __str__(self):
        """
        Возвращает строковое представление объекта "Транспорт с ДВС".
        Метод перегружен для представления новых свойств

        :return: Строковое представление объекта "Транспорт с ДВС".
        """
        return f"Транспортное средство {self._name}. Вид транспорта {self.type_of_transport.value}. " \
               f"Мощность двигателя {self._engine_power}. Вместимость бака {self._tank_volume}. " \
               f"Количество литров топлива {self._fuel_volume}."

    def __repr__(self):
        """
        Возвращает представление объекта "Транспорт с ДВС" в виде строки, которое можно использовать для
        воссоздания объекта.
        Метод перегружен для представления новых свойств

        :return: Представление объекта "Транспорт с ДВС" в виде строки.
        """
        return f"{self.__class__.__name__}(name={self._name!r}, type_of_transport={self.type_of_transport.value!r}, " \
               f"engine_power={self._engine_power!r}, tank_volume={self._tank_volume!r}, " \
               f"fuel_volume={self._fuel_volume!r})"


if __name__ == "__main__":
    doctest.testmod()
    pass
