#!/usr/bin/env python3

MIN_SPEED = 0
MIN_CAPACITY = 1
MIN_LOAD_CAPACITY = 0
MIN_TARIFF = 0
MIN_DISTANCE = 0
COST_PER_TON_KM = 10
SPEED_LIMIT = 70
DEMO_DISTANCE = 50


class Transport:
    """
    Базовый класс для любого транспорта.

    """

    def __init__(self, speed, capacity):
        """
        Инициализирует транспорт.

        :param speed: скорость транспорта (неотрицательное число).
        :param capacity: вместимость транспорта (положительное целое).
        :raises ValueError: если speed или capacity невалидны.
        """
        self._speed = None      # объявление атрибутов в конструкторе
        self._capacity = None
        self.speed = speed      # валидация через сеттер
        self.capacity = capacity

    @property
    def speed(self):
        """Возвращает скорость транспорта."""
        return self._speed

    @speed.setter
    def speed(self, value):
        """
        Устанавливает скорость с валидацией.

        :param value: новое значение скорости.
        :raises ValueError: если value не число или отрицательное.
        """
        if type(value) not in (int, float) or value < MIN_SPEED:
            raise ValueError("Скорость должна быть неотрицательным числом.")
        self._speed = value

    @property
    def capacity(self):
        """Возвращает вместимость транспорта."""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """
        Устанавливает вместимость с валидацией.

        :param value: новое значение вместимости.
        :raises ValueError: если value не целое или меньше 1.
        """
        if type(value) is not int or value < MIN_CAPACITY:
            raise ValueError("Вместимость должна быть положительным целым числом.")
        self._capacity = value

    def is_speed_exceeded(self, limit):
        """
        Проверяет, превышена ли заданная отметка скорости.

        :param limit: пороговое значение скорости.
        :return: True, если скорость превышена; False иначе.
        """
        return self.speed > limit

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект класса из словаря.

        :param data: словарь с ключами 'speed' и 'capacity'.
        :return: новый объект класса Transport.
        :raises ValueError: если ключи 'speed'/'capacity' отсутствуют.
        """
        speed = data.get("speed")
        capacity = data.get("capacity")
        if speed is None or capacity is None:
            raise ValueError("В словаре отсутствуют ключи 'speed' или 'capacity'.")
        return cls(speed=speed, capacity=capacity)

    def __str__(self):
        """
        Возвращает строковое представление транспорта.

        :return: строка с описанием транспорта.
        """
        return f"Скорость: {self.speed}, Вместимость: {self.capacity}"


class Bus(Transport):
    """
    Класс автобуса, наследующий Transport.
    """

    def __init__(self, speed, capacity, route):
        """
        Инициализирует автобус.

        :param speed: скорость автобуса.
        :param capacity: вместимость автобуса.
        :param route: маршрут автобуса (непустая строка).
        :raises ValueError: если speed/capacity невалидны или route пуст.
        """
        super().__init__(speed, capacity)
        self._route = None      # объявление атрибута
        self.route = route      # валидация через сеттер

    @property
    def route(self):
        """Возвращает маршрут автобуса."""
        return self.__route

    @route.setter
    def route(self, value):
        """
        Устанавливает маршрут с валидацией.

        :param value: новое значение маршрута.
        :raises ValueError: если value не строка или пустая.
        """
        if type(value) is not str or not value.strip():
            raise ValueError("Маршрут должен быть непустой строкой.")
        self.__route = value

    def __str__(self):
        """
        Возвращает строковое представление автобуса.

        :return: строка с описанием автобуса.
        """
        return f"{super().__str__()}, Маршрут: {self.route}"


class Truck(Transport):
    """
    Класс грузовика, наследующий Transport.
    """

    def __init__(self, speed, capacity, load_capacity):
        """
        Инициализирует грузовик.

        :param speed: скорость грузовика.
        :param capacity: вместимость грузовика.
        :param load_capacity: грузоподъёмность в тоннах.
        :raises ValueError: если speed/capacity невалидны или load_capacity <= 0.
        """
        super().__init__(speed, capacity)
        self._load_capacity = None      # объявление атрибута
        self.load_capacity = load_capacity

    @property
    def load_capacity(self):
        """Возвращает грузоподъёмность."""
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        """
        Устанавливает грузоподъёмность с валидацией.

        :param value: новое значение грузоподъёмности.
        :raises ValueError: если value не число или <= 0.
        """
        if type(value) not in (int, float) or value <= MIN_LOAD_CAPACITY:
            raise ValueError("Грузоподъёмность должна быть положительным числом.")
        self.__load_capacity = value

    def calculate_cost(self, distance):
        """
        Рассчитывает стоимость перевозки.

        :param distance: расстояние в километрах.
        :return: стоимость перевозки.
        :raises ValueError: если distance не число или <= 0.
        """
        if type(distance) not in (int, float) or distance <= MIN_DISTANCE:
            raise ValueError("Расстояние должно быть положительным числом.")
        return self.load_capacity * distance * COST_PER_TON_KM

    def __str__(self):
        """
        Возвращает строковое представление грузовика.

        :return: строка с описанием грузовика.
        """
        return f"{super().__str__()}, Грузоподъёмность: {self.load_capacity} т"


class Taxi(Transport):
    """
    Класс такси, наследующий Transport.
    """

    def __init__(self, speed, capacity, tariff):
        """
        Инициализирует такси.

        :param speed: скорость такси.
        :param capacity: вместимость такси.
        :param tariff: тариф за километр.
        :raises ValueError: если speed/capacity невалидны или tariff <= 0.
        """
        super().__init__(speed, capacity)
        self._tariff = None     # объявление атрибута
        self.tariff = tariff    # валидация через сеттер

    @property
    def tariff(self):
        """Возвращает тариф."""
        return self.__tariff

    @tariff.setter
    def tariff(self, value):
        """
        Устанавливает тариф с валидацией.

        :param value: новое значение тарифа.
        :raises ValueError: если value не число или <= 0.
        """
        if type(value) not in (int, float) or value <= MIN_TARIFF:
            raise ValueError("Тариф должен быть положительным числом.")
        self.__tariff = value

    def calculate_cost(self, distance):
        """
        Рассчитывает стоимость поездки.

        :param distance: расстояние в километрах.
        :return: стоимость поездки.
        :raises ValueError: если distance не число или <= 0.
        """
        if type(distance) not in (int, float) or distance <= MIN_DISTANCE:
            raise ValueError("Расстояние должно быть положительным числом.")
        return self.tariff * distance

    def __str__(self):
        """
        Возвращает строковое представление такси.

        :return: строка с описанием такси.
        """
        return f"{super().__str__()}, Тариф: {self.tariff} руб/км"


if __name__ == "__main__":
    print("=== 1. Создание объектов через конструктор ===")
    bus = Bus(60, 40, "Маршрут №1")
    truck = Truck(80, 2, 10)
    taxi = Taxi(100, 4, 25)

    print(bus)
    print(truck)
    print(taxi)

    print("\n=== 2. Создание объектов через классовый метод ===")
    data = {"speed": 120, "capacity": 2}
    truck2 = Transport.from_dict(data)
    print(f"Создан из словаря: {truck2}")

    print("\n=== 3. Попытка задать недопустимую скорость или вместимость ===")
    try:
        bus.speed = -10
    except ValueError as e:
        print(f"Ошибка: {e}")
    try:
        taxi.capacity = -30
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== 4. Вызов методов без создания объекта ===")
    print(f"Метод класса Transport.from_dict: {Transport.from_dict}")
    print(f"Метод экземпляра Bus.__str__: {Bus.__str__}")

    print("\n=== 5. Полиморфный вызов методов ===")
    transports = (bus, truck, taxi)

    print("\nИнформация о транспорте:")
    for t in transports:
        print(t)

    print(f"\nПроверка превышения скорости (лимит {SPEED_LIMIT}):")
    for t in transports:
        print(f"{type(t).__name__}: превышена = {t.is_speed_exceeded(SPEED_LIMIT)}")

    print(f"\nРасчёт стоимости (расстояние {DEMO_DISTANCE} км):")
    print(f"Truck: {truck.calculate_cost(DEMO_DISTANCE)} руб.")
    print(f"Taxi: {taxi.calculate_cost(DEMO_DISTANCE)} руб.")
