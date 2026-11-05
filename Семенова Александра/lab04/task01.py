#!/usr/bin/env python3

class Transport:
    """
    Класс для транспорта.

    :param speed: скорость транспорта
    :param capacity: вместимость транспорта
    """

    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Скорость должна быть неотрицательным числом.")
        self.__speed = value

    @property  #метод -> переменная
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Вместимость должна быть положительным целым числом.")
        self.__capacity = value

    def get_info(self):
        """
        Возвращает строку с основными характеристиками.

        :return: строка с описанием транспорта.
        """
        return f"Скорость: {self.speed}, Вместимость: {self.capacity}"

    def is_speed_exceeded(self, limit):
        """
        Проверяет, превышена ли заданная отметка скорости.

        :param limit: пороговое значение скорости.
        :return: True, если скорость превышена; False в противном случае.
        """
        return self.speed > limit
  
    @classmethod          # метод -> класс
    def from_dict(cls, data):
        """
        Создаёт объект класса из словаря.

        :param data: словарь с ключами 'speed' и 'capacity'.
        :return: новый объект класса Transport.
        """
        return cls(speed=data["speed"], capacity=data["capacity"])    #data - метод

class Bus(Transport):
    """
    Класс автобуса, наследующий Transport.

    :param speed: скорость автобуса.
    :param capacity: вместимость автобуса.
    :param route: маршрут автобуса.
    """

    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.route = route

    @property
    def route(self):
        return self.__route

    @route.setter
    def route(self, value):
        if type(value) is not str or not value.strip():
            raise ValueError("Маршрут должен быть непустой строкой.")
        self.__route = value

    def get_info(self):
        """
        Возвращает строку с характеристиками автобуса.

        :return: строка с описанием автобуса.
        """
        return f"{super().get_info()}, Маршрут: {self.route}"   # супер - для обращения к родительскому классу
    
class Truck(Transport):
    """
    Класс грузовика, наследующий Transport.

    :param speed: скорость грузовика.
    :param capacity: вместимость грузовика.
    :param load_capacity: грузоподъёмность в тоннах.
    """

    def __init__(self, speed, capacity, load_capacity):
        super().__init__(speed, capacity)
        self.load_capacity = load_capacity

    @property
    def load_capacity(self):
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, value):
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Грузоподъёмность должна быть положительным числом.")
        self.__load_capacity = value

    def calculate_cost(self, distance):
        """
        Рассчитывает стоимость перевозки.

        :param distance: расстояние в километрах.
        :return: стоимость перевозки.
        """
        return self.load_capacity * distance * 10

class Taxi(Transport):
    """
    Класс такси, наследующий Transport.

    :param speed: скорость такси.
    :param capacity: вместимость такси.
    :param tariff: тариф за километр.
    """

    def __init__(self, speed, capacity, tariff):
        super().__init__(speed, capacity)
        self.tariff = tariff

    @property
    def tariff(self):
        return self.__tariff

    @tariff.setter
    def tariff(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Тариф должен быть положительным числом.")
        self.__tariff = value

    def calculate_cost(self, distance):
        """
        Рассчитывает стоимость поездки.

        :param distance: расстояние в километрах.
        :return: стоимость поездки.
        """
        return self.tariff * distance

if __name__ == "__main__":
    print("=== 1. Создание объектов через конструктор ===")
    bus = Bus(60, 40, "Маршрут №1")
    truck = Truck(80, 2, 10)
    taxi = Taxi(100, 4, 25)

    print(bus.get_info())
    print(truck.get_info())
    print(taxi.get_info())

    print("\n=== 2. Создание объектов через классовый метод ===")
    data = {"speed": 120, "capacity": 2}
    truck2 = Transport.from_dict(data)
    print(f"Создан из словаря: {truck2.get_info()}")

    print("\n=== 3. Попытка задать недопустимую скорость или вместимость ===")
    try:
        bus.speed = -10
    except ValueError:
        print(f"Ошибка! Скорость не может быть отрицательной.")
    try:
        taxi.capacity = -30
    except ValueError:
        print(f"Ошибка! Вместимость не может быть отрицательной.")

    print("\n=== 4. Вызов методов без создания объекта ===")
    print(f"Метод класса Transport.from_dict: {Transport.from_dict}")
    print(f"Метод экземпляра Bus.get_info: {Bus.get_info}")

    print("\n=== 5. Полиморфный вызов методов ===")
    transports = [bus, truck, taxi]

    print("\nИнформация о транспорте:")
    for t in transports:
        print(t.get_info())

    print("\nПроверка превышения скорости (лимит 70):")
    for t in transports:
        print(f"{type(t).__name__}: превышена = {t.is_speed_exceeded(70)}")   
# t = bus type(t)          # <class '__main__.Bus'> type(t).__name__ # "Bus"

    print("\nРасчёт стоимости (расстояние 50 км):")
    print(f"Truck: {truck.calculate_cost(50)} руб.")
    print(f"Taxi: {taxi.calculate_cost(50)} руб.")

