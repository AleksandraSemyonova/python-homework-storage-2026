#!/usr/bin/env python3


import argparse
import sys

MIN_AGE = 0
MAX_AGE = 120
EXIT_CODE_INVALID_AGE = 2

DEMO_CASE_1 = {"name": "Александра", "age": 19, "formal": True}
DEMO_CASE_2 = {"name": "Иван", "age": None, "formal": False}
DEMO_CASE_3 = {"name": "Мария", "age": 25, "formal": True}
DEMO_CASE_4 = {"name": "Тест", "age": -5, "formal": False}
DEMO_CASE_5 = {"name": "Тест", "age": 150, "formal": False}


def validate_age(age):
    """
    Проверяет корректность возраста.

    Если возраст не указан (None), проверка проходит успешно.

    Args:
        age: значение возраста (int или None).

    Returns:
        bool: True, если возраст корректен, иначе False.
    """
    if age is None:
        return True
    return MIN_AGE <= age <= MAX_AGE


def format_greeting(name, age=None, formal=False):
    """
    Формирует строку приветствия для пользователя.

    Args:
        name: имя пользователя.
        age: возраст (необязательный).
        formal: флаг официального приветствия.

    Returns:
        str: сформированная строка приветствия.
    """
    greeting = f"Уважаемый(ая), {name}!" if formal else f"Привет, {name}!"
    
    if age is not None:
        greeting += f"Вам {age} лет."
    return greeting


def parse_args(argv=None):
    """
    Разбирает аргументы командной строки.

    Args:
        argv: список аргументов 

    Returns:
        argparse.Namespace: пространство имён с полями name, age, formal
    """
    parser = argparse.ArgumentParser(
        description="Скрипт приветствия пользователя."
    )
    parser.add_argument(
        "name", help="Имя пользователя (обязательный аргумент)."
    )
    parser.add_argument(
        "--age", type=int, default=None,
        help="Возраст пользователя (целое число от 0 до 120)."
    )
    parser.add_argument(
        "--formal", action="store_true",
        help="Использовать официальное приветствие ('Уважаемый(ая)')."
    )
    return parser.parse_args(argv)


def run(name, age=None, formal=False):
    """
    Выполняет валидацию возраста и выводит приветствие.

    Args:
        name: имя пользователя.
        age: возраст (необязательный).
        formal: флаг официального приветствия.

    Returns:
        str: строку приветствия, или завершает программу при ошибке.
    """
    if not validate_age(age):
        print(
            f"Ошибка: возраст должен быть целым числом от {MIN_AGE} "
            f"до {MAX_AGE}. Получено значение: {age}."
        )
        sys.exit(EXIT_CODE_INVALID_AGE)

    greeting = format_greeting(name, age, formal)
    print(greeting)
    return greeting


if __name__ == "__main__":

    print("--- Случай 1: официальное приветствие с возрастом ---")
    print(f"Параметры: {DEMO_CASE_1}")
    run(**DEMO_CASE_1)

    print("--- Случай 2: неформальное приветствие без возраста ---")
    print(f"Параметры: {DEMO_CASE_2}")
    run(**DEMO_CASE_2)

    print("--- Случай 3: официальное приветствие с возрастом ---")
    print(f"Параметры: {DEMO_CASE_3}")
    run(**DEMO_CASE_3)

    print("--- Случай 4: некорректный возраст (отрицательный) ---")
    print(f"Параметры: {DEMO_CASE_4}")
    if not validate_age(DEMO_CASE_4["age"]):
        print(
            f"Ошибка: возраст должен быть целым числом от {MIN_AGE} "
            f"до {MAX_AGE}. Получено значение: {DEMO_CASE_4['age']}."
        )

    print("--- Случай 5: некорректный возраст (слишком большой) ---")
    print(f"Параметры: {DEMO_CASE_5}")
    if not validate_age(DEMO_CASE_5["age"]):
        print(
            f"Ошибка: возраст должен быть целым числом от {MIN_AGE} "
            f"до {MAX_AGE}. Получено значение: {DEMO_CASE_5['age']}."
        )


