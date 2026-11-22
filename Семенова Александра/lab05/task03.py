#!/usr/bin/env python3

import argparse


ERROR_NO_STRINGS = "Ошибка: не передано ни одной строки. Укажите хотя бы один аргумент."

TEST_STRINGS = ("яблоко", "банан", "яблоко", "киви", "ананас", "груша", "айва")
TEST_UNIQUE = True
TEST_MIN_LENGTH = 4
TEST_SORT = "asc"
TEST_COUNT = False
MIN_LENGTH_THRESHOLD = 0

SORT_ASC = "asc"
SORT_DESC = "desc"
SORT_NONE = "none"
VALID_SORT_MODES = (SORT_ASC, SORT_DESC, SORT_NONE)


def parse_args(argv=None):
    """
    Парсит аргументы командной строки.

    Args:
        argv: список аргументов.

    Returns:
        argparse.Namespace: объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        description="Обработка строковых аргументов с фильтрацией и сортировкой."
    )
    parser.add_argument(
        "strings",
        nargs="*",
        help="Одна или несколько строк для обработки.",
    )
    parser.add_argument(
        "--count",
        action="store_true",
        help="Вывести только количество строк после применения фильтров.",
    )
    parser.add_argument(
        "--unique",
        action="store_true",
        help="Выводить только уникальные строки.",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=0,
        help="Минимальная длина строк для вывода.",
    )
    parser.add_argument(
        "--sort",
        choices=VALID_SORT_MODES,
        default=SORT_NONE,
        help="Сортировка строк: asc (по возрастанию), desc (по убыванию), none (без сортировки).",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Запустить с тестовым набором данных.",
    )
    return parser.parse_args(argv)


def filter_strings(strings, unique, min_length):
    """
    Применяет фильтры к списку строк.

    Args:
        strings: исходный список строк.
        unique: если True, оставить только уникальные строки.
        min_length: минимальная допустимая длина строки.

    Returns:
        list: отфильтрованный список строк.
    """
    result = strings

    if unique:
        seen = set()
        unique_list = []
        for s in result:
            if s not in seen:
                seen.add(s)
                unique_list.append(s)
        result = unique_list

    if min_length > MIN_LENGTH_THRESHOLD:
        result = [s for s in result if len(s) >= min_length]

    return result


def sort_strings(strings, mode):
    """
    Сортирует список строк согласно указанному режиму.

    Args:
        strings: список строк.
        mode: режим сортировки ('asc', 'desc', 'none').

    Returns:
        list: отсортированный (или исходный) список строк.
    """
    if mode == SORT_ASC:
        return sorted(strings)
    elif mode == SORT_DESC:
        return sorted(strings, reverse=True)
    return strings


def run(strings, count=False, unique=False, min_length=0, sort=SORT_NONE):
    """
    Выполняет фильтрацию, сортировку и вывод строк.

    Args:
        strings: список строк.
        count: если True, вывести только количество.
        unique: если True, оставить только уникальные.
        min_length: минимальная длина строки.
        sort: режим сортировки.
    """
    filtered = filter_strings(strings, unique, min_length)
    result = sort_strings(filtered, sort)

    if count:
        print(len(result))
    else:
        for s in result:
            print(s)


if __name__ == "__main__":
    args = parse_args()

    if args.test:
        args.strings = TEST_STRINGS
        args.unique = TEST_UNIQUE
        args.min_length = TEST_MIN_LENGTH
        args.sort = TEST_SORT
        args.count = TEST_COUNT

    if not args.strings:
        print(ERROR_NO_STRINGS)
        raise SystemExit(1)

    run(
        strings=args.strings,
        count=args.count,
        unique=args.unique,
        min_length=args.min_length,
        sort=args.sort,
    )

