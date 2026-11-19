#!/usr/bin/env python3


import argparse
import os

VALID_OPERATIONS = ("add", "sub", "mul", "div")
DEFAULT_PRECISION = 2
DEFAULT_FILENAME = "history.txt"

DEMO_CALC_1 = {
    "x": 10.5, "y": 3.2, "operation": "add",
    "precision": 2, "filename": DEFAULT_FILENAME
}
DEMO_CALC_2 = {
    "x": 100, "y": 7, "operation": "div",
    "precision": 7, "filename": DEFAULT_FILENAME
}
DEMO_CALC_3 = {
    "x": 5, "y": 0, "operation": "div",
    "precision": 2, "filename": DEFAULT_FILENAME
}
DEMO_CALC_4 = {
    "x": 8, "y": 4, "operation": None,
    "precision": 2, "filename": DEFAULT_FILENAME
}
DEMO_CALC_5 = {
    "x": 12.34567, "y": 2.1, "operation": "mul",
    "precision": 3, "filename": DEFAULT_FILENAME
}


def calculate(x, y, operation="add", precision=DEFAULT_PRECISION):
    """
    Выполняет арифметическую операцию над двумя числами.

    Args:
        x: первое число.
        y: второе число.
        operation: операция (add/sub/mul/div). По умолчанию 'add'.
        precision: количество знаков после запятой.

    Returns:
        tuple: (result, error_message). Если операция выполнена
            успешно, error_message равно None. При делении на ноль
            result равно None.
    """
    if operation is None:
        return (x, y), None

    operations = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b,
    }

    try:
        result = operations[operation](x, y)
        return round(result, precision), None
    except ZeroDivisionError:
        return None, f"Ошибка: деление на ноль ({x} / {y})."


def format_result(x, y, operation, result, precision):
    """
    Форматирует строку с результатом операции.

    Args:
        x: первое число (операнд).
        y: второе число (операнд).
        operation: название операции.
        result: результат вычисления.
        precision: точность округления.

    Returns:
        str: отформатированная строка с результатом.
    """
    if operation is None:
        return f"x = {round(x, precision)}, y = {round(y, precision)}"

    symbols = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
    symbol = symbols.get(operation, operation)
    return f"{round(x, precision)} {symbol} {round(y, precision)} = {result}"


def save_to_file(line, filename):
    """
    Дописывает строку результата в файл истории.

    Args:
        line: строка для записи.
        filename: имя файла для сохранения.
    """
    def save_to_file(line, filename):
     entry = f"{line}\n"
     with open(filename, "a", encoding="utf-8") as f:
        f.write(entry)


def parse_args(argv=None):
    """
    Разбирает аргументы командной строки для калькулятора.

    Args:
        argv: список аргументов (по умолчанию sys.argv[1:]).

    Returns:
        argparse.Namespace: пространство имён с полями x, y,
            operation, precision, filename.
    """
    parser = argparse.ArgumentParser(
        description="Калькулятор с сохранением истории."
    )
    parser.add_argument("x", type=float, help="Первое число.")
    parser.add_argument("y", type=float, help="Второе число.")
    parser.add_argument(
        "--operation", choices=VALID_OPERATIONS, default=None,
        help="Операция: add, sub, mul, div. Если не указана — "
             "выводятся оба числа."
    )
    parser.add_argument(
        "--precision", type=int, default=DEFAULT_PRECISION,
        help=f"Количество знаков после запятой "
             f"(по умолчанию {DEFAULT_PRECISION})."
    )
    parser.add_argument(
        "--filename", type=str, default=DEFAULT_FILENAME,
        help=f"Имя файла для сохранения "
             f"(по умолчанию '{DEFAULT_FILENAME}')."
    )
    return parser.parse_args(argv)


def run(x, y, operation=None, precision=DEFAULT_PRECISION,
        filename=DEFAULT_FILENAME):
    """
    Выполняет вычисление, выводит и сохраняет результат.

    Args:
        x: первое число.
        y: второе число.
        operation: операция (add/sub/mul/div) или None.
        precision: точность округления.
        filename: имя файла для сохранения истории.
    """
    result, error = calculate(x, y, operation, precision)

    if error:
        save_to_file(f"ОШИБКА: {error}", filename)
        return

    line = format_result(x, y, operation, result, precision)
    
    if operation is None:
        print(f"Операция не указана. Числа: {line}")
    else:
        print(f"Результат: {line}")

    save_to_file(line, filename)
    print(f"Результат сохранён в файл '{filename}'.")


if __name__ == "__main__":

    print("--- Случай 1: сложение ---")
    print(f"Параметры: {DEMO_CALC_1}")
    run(**DEMO_CALC_1)
  

    print("--- Случай 2: деление с точностью 4 знака ---")
    print(f"Параметры: {DEMO_CALC_2}")
    run(**DEMO_CALC_2)
   
    print("--- Случай 3: деление на ноль ---")
    print(f"Параметры: {DEMO_CALC_3}")
    run(**DEMO_CALC_3)


    print("--- Случай 4: операция не указана ---")
    print(f"Параметры: {DEMO_CALC_4}")
    run(**DEMO_CALC_4)
  

    print("--- Случай 5: умножение с точностью 3 знака ---")
    print(f"Параметры: {DEMO_CALC_5}")
    run(**DEMO_CALC_5)
    


