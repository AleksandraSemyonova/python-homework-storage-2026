#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random

VALID_GENDERS = ("мужской", "женский", "М", "Ж", "male", "female")
RETIREMENT_AGE = 60
ADULT_AGE = 18
MIN_AGE = 0
MAX_AGE = 100
MONTHS_IN_YEAR = 12


class Person(ABC):
    """
    Абстрактный базовый класс для человека.
    """

    def __init__(self, name, gender, age):
        """
        Инициализирует человека.

        :param name: имя человека (непустая строка).
        :param gender: пол человека (одно из допустимых значений).
        :param age: возраст человека (число от 0 до 100).
        :raises ValueError: если name, gender или age невалидны.
        """
        self._name = None
        self._gender = None
        self._age = None
        self.name = name
        self.gender = gender
        self.age = age

    @property
    def name(self):
        """Возвращает имя человека."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Устанавливает имя с валидацией.

        :param value: новое значение имени.
        :raises ValueError: если value не строка или пустая.
        """
        if type(value) is not str or not value.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        self._name = value.strip()

    @property
    def gender(self):
        """Возвращает пол человека."""
        return self._gender

    @gender.setter
    def gender(self, value):
        """
        Устанавливает пол с валидацией.

        :param value: новое значение пола.
        :raises ValueError: если value не строка или недопустимое значение.
        """
        if type(value) is not str or value.lower() not in VALID_GENDERS:
            raise ValueError(
                f"Недопустимое значение пола. Допустимые: {VALID_GENDERS}"
            )
        self._gender = value.lower()

    @property
    def age(self):
        """Возвращает возраст человека."""
        return self._age

    @age.setter
    def age(self, value):
        """
        Устанавливает возраст с валидацией.

        :param value: новое значение возраста.
        :raises ValueError: если value не число или вне диапазона.
        """
        if type(value) not in (int, float) or value < MIN_AGE or value > MAX_AGE:
            raise ValueError(
                f"Возраст должен быть числом от {MIN_AGE} до {MAX_AGE}."
            )
        self._age = value

    def is_adult(self):
        """
        Проверяет совершеннолетие.

        :return: True, если возраст >= ADULT_AGE; False в противном случае.
        """
        return self.age >= ADULT_AGE

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект класса из словаря.

        :param data: словарь с ключами 'name', 'gender' и полями класса.
        :return: новый объект класса.
        :raises ValueError: если ключи 'name' или 'gender' отсутствуют.
        """
        name = data.get("name")
        gender = data.get("gender")
        if name is None or gender is None:
            raise ValueError(
                "В словаре отсутствуют обязательные ключи 'name' или 'gender'."
            )
        return cls(**data)

    @abstractmethod
    def __str__(self):
        """
        Возвращает строковое представление человека.

        :return: строка с описанием.
        """
        return f"Имя: {self.name}, Пол: {self.gender}, Возраст: {self.age}"


class Employee(Person):
    """
    Класс сотрудника, наследующий Person.
    
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        """
        Инициализирует сотрудника.

        :param name: имя сотрудника.
        :param gender: пол сотрудника.
        :param age: возраст сотрудника.
        :param position: должность (непустая строка).
        :param salary: зарплата (неотрицательное число).
        :param monthly_expenses: ежемесячные расходы (неотрицательное число).
        :raises ValueError: если любой из параметров невалиден.
        """
        super().__init__(name, gender, age)
        self._position = None
        self._salary = None
        self._monthly_expenses = None
        self.position = position
        self.salary = salary
        self.monthly_expenses = monthly_expenses

    @property
    def position(self):
        """Возвращает должность."""
        return self._position

    @position.setter
    def position(self, value):
        """
        Устанавливает должность с валидацией.

        :param value: новое значение должности.
        :raises ValueError: если value не строка или пустая.
        """
        if type(value) is not str or not value.strip():
            raise ValueError("Должность должна быть непустой строкой.")
        self._position = value.strip()

    @property
    def salary(self):
        """Возвращает зарплату."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """
        Устанавливает зарплату с валидацией.

        :param value: новое значение зарплаты.
        :raises ValueError: если value не число или отрицательное.
        """
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом.")
        self._salary = value

    @property
    def monthly_expenses(self):
        """Возвращает ежемесячные расходы."""
        return self._monthly_expenses

    @monthly_expenses.setter
    def monthly_expenses(self, value):
        """
        Устанавливает расходы с валидацией.

        :param value: новое значение расходов.
        :raises ValueError: если value не число или отрицательное.
        """
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Расходы должны быть неотрицательным числом.")
        self._monthly_expenses = value

    def income_for_months(self, n):
        """
        Оценивает приток денег за N месяцев.

        :param n: количество месяцев (положительное целое).
        :return: сумма притока за N месяцев.
        :raises ValueError: если n не положительное целое.
        """
        if type(n) is not int or n <= 0:
            raise ValueError(
                "Количество месяцев должно быть положительным целым числом."
            )
        return self.salary * n

    def check_survival(self):
        """
        Проверяет, хватает ли зарплаты на расходы.

        :return: True, если сотрудник "выживает"; False в противном случае.
        """
        return self.salary >= self.monthly_expenses

    def savings_until_retirement(self):
        """
        Рассчитывает, сколько человек скопит до пенсии.

        :return: сумма накоплений до пенсионного возраста.
        """
        if self.age >= RETIREMENT_AGE:
            return 0
        years_left = RETIREMENT_AGE - self.age
        months_left = years_left * MONTHS_IN_YEAR
        monthly_savings = self.salary - self.monthly_expenses
        if monthly_savings <= 0:
            return 0
        return monthly_savings * months_left

    def __str__(self):
        """
        Возвращает строку с информацией о сотруднике.

        :return: строка с описанием.
        """
        return f"{super().__str__()}, Должность: {self.position}, " \
               f"Зарплата: {self.salary}, Расходы: {self.monthly_expenses}"


class Manager(Employee):
    """
    Класс менеджера, наследующий Employee.

    """

    def __init__(self, name, gender, age, position, salary,
                 monthly_expenses, subordinates=None):
        """
        Инициализирует менеджера.

        :param name: имя менеджера.
        :param gender: пол менеджера.
        :param age: возраст менеджера.
        :param position: должность.
        :param salary: зарплата.
        :param monthly_expenses: расходы.
        :param subordinates: список подчинённых (по умолчанию пустой).
        :raises ValueError: если subordinates не список.
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__subordinates = None
        self.subordinates = subordinates if subordinates is not None else []

    @property
    def subordinates(self):
        """Возвращает список подчинённых."""
        return self.__subordinates

    @subordinates.setter
    def subordinates(self, value):
        """
        Устанавливает список подчинённых.

        :param value: список подчинённых.
        :raises ValueError: если value не список.
        """
        if type(value) is not list:
            raise ValueError("Подчинённые должны быть списком.")
        self.__subordinates = value

    def add_subordinate(self, employee):
        """
        Добавляет подчинённого.

        :param employee: сотрудник.
        """
        self.subordinates.append(employee)
        print(f"{employee.name} добавлен в подчинение к {self.name}.")

    def remove_subordinate(self, employee):
        """
        Удаляет подчинённого.

        :param employee: сотрудник.
        """
        if employee in self.subordinates:
            self.subordinates.remove(employee)
            print(f"{employee.name} уволен из подчинения {self.name}.")
        else:
            print(f"{employee.name} не числится в подчинении {self.name}.")

    def hold_meeting(self, topic):
        """
        Проводит митинг с подчинёнными.

        :param topic: тема митинга.
        """
        print(f"\n=== Митинг у {self.name} ===")
        print(f"Тема: {topic}")
        print(f"Участники ({len(self.subordinates)} чел.):")
        for sub in self.subordinates:
            print(f" - {sub.name} ({sub.position})")

    def work(self):
        """Метод работы менеджера."""
        print(
            f"{self.name} (Manager) проводит совещание с "
            f"{len(self.subordinates)} подчинёнными."
        )

    def __str__(self):
        """Возвращает информацию о менеджере."""
        return f"{super().__str__()}, Подчинённых: {len(self.subordinates)}"


class Developer(Employee):
    """
    Класс разработчика, наследующий Employee.
    
    """

    def __init__(self, name, gender, age, position, salary,
                 monthly_expenses, languages=None):
        """
        Инициализирует разработчика.

        :param name: имя разработчика.
        :param gender: пол разработчика.
        :param age: возраст разработчика.
        :param position: должность.
        :param salary: зарплата.
        :param monthly_expenses: расходы.
        :param languages: список языков программирования.
        :raises ValueError: если languages не список.
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__languages = None
        self.languages = languages if languages is not None else []

    @property
    def languages(self):
        """Возвращает список языков."""
        return self.__languages

    @languages.setter
    def languages(self, value):
        """
        Устанавливает список языков.

        :param value: список языков.
        :raises ValueError: если value не список.
        """
        if type(value) is not list:
            raise ValueError("Языки должны быть списком.")
        self.__languages = value

    def add_language(self, language):
        """
        Добавляет язык программирования.

        :param language: название языка.
        :raises ValueError: если language не строка или пустая.
        """
        if type(language) is not str or not language.strip():
            raise ValueError("Язык должен быть непустой строкой.")
        if language not in self.languages:
            self.languages.append(language)

    def write_code(self):
        """
        Пишет код на случайном языке из списка.

        :return: выбранный язык или None, если список пуст.
        """
        if not self.languages:
            print(f"{self.name} не знает ни одного языка программирования.")
            return None
        lang = random.choice(self.languages)
        print(f"{self.name} пишет код на {lang}.")
        return lang

    def work(self):
        """Метод работы разработчика."""
        self.write_code()

    def __str__(self):
        """Возвращает информацию о разработчике."""
        langs = ", ".join(self.languages) if self.languages else "нет"
        return f"{super().__str__()}, Языки: {langs}"


class Designer(Employee):
    """
    Класс дизайнера, наследующий Employee.

    Добавляет список инструментов. Поле tools объявлено как
    private (__tools), потому что оно уникально для дизайнера.
    """

    def __init__(self, name, gender, age, position, salary,
                 monthly_expenses, tools=None):
        """
        Инициализирует дизайнера.

        :param name: имя дизайнера.
        :param gender: пол дизайнера.
        :param age: возраст дизайнера.
        :param position: должность.
        :param salary: зарплата.
        :param monthly_expenses: расходы.
        :param tools: список инструментов.
        :raises ValueError: если tools не список.
        """
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.__tools = None
        self.tools = tools if tools is not None else []

    @property
    def tools(self):
        """Возвращает список инструментов."""
        return self.__tools

    @tools.setter
    def tools(self, value):
        """
        Устанавливает список инструментов.

        :param value: список инструментов.
        :raises ValueError: если value не список.
        """
        if type(value) is not list:
            raise ValueError("Инструменты должны быть списком.")
        self.__tools = value

    def add_tool(self, tool):
        """
        Добавляет инструмент.

        :param tool: название инструмента.
        :raises ValueError: если tool не строка или пустая.
        """
        if type(tool) is not str or not tool.strip():
            raise ValueError("Инструмент должен быть непустой строкой.")
        if tool not in self.tools:
            self.tools.append(tool)

    def create_mockup(self, project_name):
        """
        Создаёт макет проекта.

        :param project_name: название проекта.
        """
        if not self.tools:
            print(f"{self.name} не имеет инструментов для работы.")
            return
        tool = random.choice(self.tools)
        print(f"{self.name} создаёт макет '{project_name}' с помощью {tool}.")

    def work(self):
        """Метод работы дизайнера."""
        self.create_mockup("Новый проект")

    def __str__(self):
        """Возвращает информацию о дизайнере."""
        tools = ", ".join(self.tools) if self.tools else "нет"
        return f"{super().__str__()}, Инструменты: {tools}"


if __name__ == "__main__":
    print("=== 1. Создание объектов через конструктор ===")
    manager = Manager(
        "Анна", "женский", 35, "Руководитель отдела", 150000, 60000
    )
    dev = Developer(
        "Иван", "мужской", 28, "Senior Developer", 120000, 50000,
        ["JavaScript", "С"]
    )
    designer = Designer(
        "Мария", "женский", 30, "UI/UX Designer", 100000, 45000,
        ["Figma", "Photoshop", "Illustrator"]
    )

    print(manager)
    print(dev)
    print(designer)

    print("\n=== 2. Создание объекта через классовый метод from_dict ===")
    data = {
        "name": "Пётр", "gender": "мужской", "age": 45,
        "position": "Аналитик", "salary": 90000, "monthly_expenses": 50000
    }
    analyst = Employee.from_dict(data)
    print(analyst)

    print("\n=== 3. Проверка совершеннолетия ===")
    print(f"{dev.name} совершеннолетний: {dev.is_adult()}")
    young = Employee("Лена", "женский", 16, "Стажёр", 0, 0)
    print(f"{young.name} совершеннолетняя: {young.is_adult()}")

    print("\n=== 4. Попытка задать невалидные данные ===")
    try:
        dev.age = -5
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        manager.gender = "робот"
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        designer.salary = -1000
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\n=== 5. Приток денег за N месяцев ===")
    print(f"Доход {dev.name} за 6 месяцев: {dev.income_for_months(6)}")
    print(
        f"Доход {designer.name} за 12 месяцев: "
        f"{designer.income_for_months(12)}"
    )

    print("\n=== 6. Проверка выживания ===")
    if dev.check_survival():
        print(f"{dev.name} финансово стабилен.")
    else:
        print(f"{dev.name} тратит больше, чем получает.")

    print("\n=== 7. Попытка 'умереть' от расходов ===")
    poor_dev = Developer("Бедный Вася", "мужской", 25, "Junior", 30000, 50000)
    if poor_dev.check_survival():
        print(f"{poor_dev.name} финансово стабилен.")
    else:
        print(
            f"{poor_dev.name} тратит {poor_dev.monthly_expenses} в месяц, "
            f"а получает {poor_dev.salary}. "
            f"Сотрудник 'умер' от финансового кризиса!"
        )

    print("\n=== 8. Накопления до пенсии ===")
    print(f"{dev.name} скопит до пенсии: {dev.savings_until_retirement()}")
    print(f"{manager.name} скопит до пенсии: {manager.savings_until_retirement()}")

    print("\n=== 9. Работа Manager ===")
    manager.add_subordinate(dev)
    manager.add_subordinate(designer)
    manager.hold_meeting("Обсуждение нового проекта")
    manager.remove_subordinate(designer)

    print("\n=== 10. Работа Developer ===")
    dev.write_code()
    dev.add_language("Rust")
    dev.write_code()

    print("\n=== 11. Работа Designer ===")
    designer.create_mockup("Афиша")
    designer.add_tool("Blender")
    designer.create_mockup("Обложка альбома")

    print("\n=== 12. Полиморфный вызов __str__ ===")
    employees = (manager, dev, designer)
    for emp in employees:
        print(emp)

    print("\n=== 13. Полиморфный вызов метода work() ===")
    for emp in employees:
        print("\n=== 14. Проверка super() в цепочке наследования ===")
        print("Manager.__str__() вызывает Employee.__str__() -> Person.__str__():")
        print(manager)
        print("Developer.__str__() вызывает Employee.__str__() -> Person.__str__():")
        print(dev)
        print("Designer.__str__() вызывает Employee.__str__() -> Person.__str__():")
        print(designer)


