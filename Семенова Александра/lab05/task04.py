#!/usr/bin/env python3

import argparse


ERROR_EMPTY_OLD = "Строка OLD не может быть пустой."
ERROR_BAD_FORMAT = "Некорректный формат строки. Ожидается 'OLD=NEW'."

DEMO_LINE_1 = "apple=fruit"
DEMO_LINE_2 = "=empty_old"
DEMO_LINE_3 = "no_equals_sign"
DEMO_LINE_4 = "banana=yellow_fruit"


def parse_line(line):
    """
    Парсит строку формата 'OLD=NEW'.

    Args:
        line: строка для парсинга.

    Returns:
        dict: словарь с ключами 'old' и 'new'.

    Raises:
        ValueError: если формат некорректный или OLD пустая.
    """
    parts = line.split("=", 1)
    if len(parts) != 2:
        raise ValueError(ERROR_BAD_FORMAT)

    old, new = parts[0], parts[1]
    if not old:
        raise ValueError(ERROR_EMPTY_OLD)

    return {"old": old, "new": new}


def parse_args(argv=None):
    """
    Разбирает аргументы командной строки.

    Args:
        argv: список аргументов.

    Returns:
        argparse.Namespace: пространство имён с полем lines.
    """
    parser = argparse.ArgumentParser(
        description="Парсер строк формата OLD=NEW."
    )
    parser.add_argument(
        "lines",
        nargs="+",
        help="Одна или несколько строк формата 'OLD=NEW'."
    )
    return parser.parse_args(argv)


def run(lines):
    """
    Парсит список строк и выводит результат.

    Args:
        lines: список строк для парсинга.
    """
    for line in lines:
        try:
            result = parse_line(line)
            print(f"OLD: '{result['old']}', NEW: '{result['new']}'")
        except ValueError as e:
            print(f"Ошибка при разборе '{line}': {e}")


if __name__ == "__main__":
    args = parse_args()
    run(args.lines)

