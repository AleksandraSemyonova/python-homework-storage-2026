#!/usr/bin/env python3

from abc import ABC, abstractmethod
import random


class Person(ABC):
    """
    Базовый класс для человека.

    :param name: имя человека.
    :param gender: пол человека.
    :param age: возраст человека.
    """

    VALID_GENDERS = ("мужской", "женский", "М", "Ж", "male", "female")
    RETIREMENT_AGE = 60

    
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """Устанавливает имя с валидацией."""
        if type(value) is not str or not value.strip():
            raise ValueError("Имя должно быть непустой строкой.")
        self.__name = value.strip()

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        """Устанавливает пол с валидацией."""
        if type(value) is not str or value.lower() not in self.VALID_GENDERS:
            raise ValueError(f"Недопустимое значение пола. Допустимые: {self.VALID_GENDERS}")
        self.__gender = value.lower()

    def is_adult(self):
        """
        Проверяет совершеннолетие.

        :return: True, если возраст >= 18; False в противном случае.
        """
        return self.age >= 18
    
    def get_info(self):  
        """Возвращает строку с основной информацией о человеке."""
        return f"Имя: {self.name}, Пол: {self.gender}, Возраст: {self.age}"

    @classmethod
    def from_variables(cls, name, gender, age):
        """
        Создаёт объект класса из переменных.

        :param name: имя.
        :param gender: пол.
        :param age: возраст.
        :return: новый объект класса.
        """
        return cls(name=name, gender=gender, age=age)
    
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        """Устанавливает возраст с валидацией."""
        if type(value) not in (int, float) or value < 0 or value > 100:
            raise ValueError("Возраст должен быть числом от 0 до 100.")
        self.__age = int(value)

    def is_adult(self):
        """
        Проверяет совершеннолетие.

        :return: True, если возраст >= 18; False в противном случае.
        """
        return self.age >= 18

    def get_info(self):
        """
        Возвращает строку с основной информацией о человеке.

        :return: строка с описанием.
        """
        return f"Имя: {self.name}, Пол: {self.gender}, Возраст: {self.age}"

    @classmethod
    def from_variables(cls, name, gender, age):
        """
        Создаёт объект класса из переменных.

        :param name: имя.
        :param gender: пол.
        :param age: возраст.
        :return: новый объект класса.
        """
        return cls(name=name, gender=gender, age=age)

class Employee(Person):
    """
    Класс сотрудника, наследующий Person.

    :param name: имя.
    :param gender: пол.
    :param age: возраст.
    :param position: должность.
    :param salary: зарплата.
    :param monthly_expenses: усреднённые расходы в месяц.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses):
        super().__init__(name, gender, age)
        self.position = position
        self.salary = salary
        self.monthly_expenses = monthly_expenses

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Устанавливает должность с валидацией."""
        if type(value) is not str or not value.strip():
            raise ValueError("Должность должна быть непустой строкой.")
        self.__position = value.strip()

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        """Устанавливает зарплату с валидацией."""
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом.")
        self.__salary = value

    @property
    def monthly_expenses(self):
        return self.__monthly_expenses

    @monthly_expenses.setter
    def monthly_expenses(self, value):
        """Устанавливает расходы с валидацией."""
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Расходы должны быть неотрицательным числом.")
        self.__monthly_expenses = value


    def income_for_months(self, n):
        """
        Оценивает приток денег за N месяцев.

        :param n: количество месяцев.
        :return: сумма притока за N месяцев.
        """
        if type(n) is not int or n <= 0:
            raise ValueError("Количество месяцев должно быть положительным целым числом.")
        return self.salary * n

    def check_survival(self):
        """
        Проверяет, хватает ли зарплаты на расходы.

        :return: True, если сотрудник "выживает"; False в противном случае.
        """
        if self.monthly_expenses > self.salary:
            raise RuntimeError(
                f"{self.name} тратит {self.monthly_expenses} в месяц, "
                f"а получает {self.salary}. Сотрудник 'умер' от финансового кризиса!"
            )
        return True

    
    def savings_until_retirement(self):
        """
        Рассчитывает, сколько человек скопит до пенсии.

        :return: сумма накоплений до пенсионного возраста.
        """
        if self.age >= self.RETIREMENT_AGE:
            return 0
        years_left = self.RETIREMENT_AGE - self.age
        months_left = years_left * 12
        monthly_savings = self.salary - self.monthly_expenses
        if monthly_savings <= 0:
            return 0
        return monthly_savings * months_left

    def get_info(self):
        """
        Возвращает строку с информацией о сотруднике.

        :return: строка с описанием.
        """
        return (f"{super().get_info()}, Должность: {self.position}, "
                f"Зарплата: {self.salary}, Расходы: {self.monthly_expenses}")

class Manager(Employee):
    """
    Класс менеджера, наследующий Employee.

    :param name: имя.
    :param gender: пол.
    :param age: возраст.
    :param position: должность.
    :param salary: зарплата.
    :param monthly_expenses: расходы.
    :param subordinates: список подчинённых.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, subordinates=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.subordinates = subordinates if subordinates is not None else []

    @property
    def subordinates(self):
        """Возвращает список подчинённых."""
        return self.__subordinates

    @subordinates.setter
    def subordinates(self, value):
        """Устанавливает список подчинённых."""
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
        print(f"{self.name} (Manager) проводит совещание с {len(self.subordinates)} подчинёнными.")

    def get_info(self):
        """Возвращает информацию о менеджере."""
        return f"{super().get_info()}, Подчинённых: {len(self.subordinates)}"

class Developer(Employee):
    """
    Класс разработчика, наследующий Employee.

    :param name: имя.
    :param gender: пол.
    :param age: возраст.
    :param position: должность.
    :param salary: зарплата.
    :param monthly_expenses: расходы.
    :param languages: список языков программирования.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, languages=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.languages = languages if languages is not None else []

    @property
    def languages(self):
        """Возвращает список языков."""
        return self.__languages

    @languages.setter
    def languages(self, value):
        """Устанавливает список языков."""
        if type(value) is not list:
            raise ValueError("Языки должны быть списком.")
        self.__languages = value

    def add_language(self, language):
        """
        Добавляет язык программирования.

        :param language: название языка.
        """
        if type(language) is not str or not language.strip():
            raise ValueError("Язык должен быть непустой строкой.")
        if language not in self.languages:
            self.languages.append(language)

    def write_code(self):
        """
        Пишет код на случайном языке из списка.

        :return: выбранный язык.
        """
        if not self.languages:
            print(f"{self.name} не знает ни одного языка программирования.")
            return None
        lang = random.choice(self.languages)
        print(f"{self.name} пишет код на {lang}.")
        return lang

    def work(self):
        self.write_code()

    def get_info(self):
        return f"{super().get_info()}, Языки: {', '.join(self.languages) if self.languages else 'нет'}"   

class Designer(Employee):
    """
    Класс дизайнера, наследующий Employee.

    :param name: имя.
    :param gender: пол.
    :param age: возраст.
    :param position: должность.
    :param salary: зарплата.
    :param monthly_expenses: расходы.
    :param tools: список инструментов.
    """

    def __init__(self, name, gender, age, position, salary, monthly_expenses, tools=None):
        super().__init__(name, gender, age, position, salary, monthly_expenses)
        self.tools = tools if tools is not None else []

    @property
    def tools(self):
        return self.__tools

    @tools.setter
    def tools(self, value):
        if type(value) is not list:
            raise ValueError("Инструменты должны быть списком.")
        self.__tools = value

    def add_tool(self, tool):
        """
        Добавляет инструмент.

        :param tool: название инструмента.
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
        self.create_mockup("Новый проект")

    def get_info(self):
        return f"{super().get_info()}, Инструменты: {', '.join(self.tools) if self.tools else 'нет'}"

if __name__ == "__main__":
    print("=== 1. Создание объектов через конструктор ===")
    manager = Manager("Анна", "женский", 35, "Руководитель отдела", 150000, 60000)
    dev = Developer("Иван", "мужской", 28, "Senior Developer", 120000, 50000,
                    ["JavaScript", "С"])
    designer = Designer("Мария", "женский", 30, "UI/UX Designer", 100000, 45000,
                        ["Figma", "Photoshop", "Illustrator"])

    print(manager.get_info())
    print(dev.get_info())
    print(designer.get_info())

    print("\n=== 2. Создание объекта через классовый метод ===")
    person = Person.from_variables("Пётр", "мужской", 45)
    print(person.get_info())

    print("\n=== 3. Проверка совершеннолетия ===")
    print(f"{dev.name} совершеннолетний: {dev.is_adult()}")
    young = Person.from_variables("Лена", "женский", 16)
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
    print(f"Доход {designer.name} за 12 месяцев: {designer.income_for_months(12)}")

    print("\n=== 6. Проверка выживания ===")
    try:
        dev.check_survival()
        print(f"{dev.name} финансово стабилен.")
    except RuntimeError as e:
        print(e)

    print("\n=== 7. Попытка 'умереть' от расходов ===")
    poor_dev = Developer("Бедный Вася", "мужской", 25, "Junior", 30000, 50000)
    try:
        poor_dev.check_survival()
    except RuntimeError as e:
        print(e)

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

    print("\n=== 12. Полиморфный вызов метода get_info() ===")
    employees = [manager, dev, designer]
    for emp in employees:
        print(emp.get_info())

    print("\n=== 13. Полиморфный вызов метода work() ===")
    for emp in employees:
        emp.work()

    print("\n=== 14. Проверка super() в цепочке наследования ===")
    print(f"\nManager.get_info() вызывает Employee.get_info() - Person.get_info():")
    print(manager.get_info())
    print(f"\nDeveloper.get_info() вызывает Employee.get_info() - Person.get_info():")
    print(dev.get_info())
    print(f"\nDesigner.get_info() вызывает Employee.get_info() - Person.get_info():")
    print(designer.get_info())

