#!/usr/bin/env python3

import argparse
import sys


ERROR_NO_STRINGS = "Ошибка: не передано ни одной строки. Укажите хотя бы один аргумент."

TEST_STRINGS = ["яблоко", "банан", "яблоко", "киви", "ананас", "груша", "айва"]
TEST_UNIQUE = True
TEST_MIN_LENGTH = 4
TEST_SORT = "asc"
TEST_COUNT = False
MIN_LENGTH_THRESHOLD = 0

def parse_args():
    """
    Парсит аргументы командной строки.

    :return: объект Namespace с разобранными аргументами.
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
        choices=["asc", "desc", "none"],
        default="none",
        help="Сортировка строк: asc (по возрастанию), desc (по убыванию), none (без сортировки).",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Запустить с тестовым набором данных.",
    )
    return parser.parse_args()


def filter_strings(strings, unique, min_length):
    """
    Применяет фильтры к списку строк.

    :param strings: исходный список строк.
    :param unique: если True, оставить только уникальные строки.
    :param min_length: минимальная допустимая длина строки.
    :return: отфильтрованный список строк.
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

    :param strings: список строк.
    :param mode: режим сортировки ('asc', 'desc', 'none').
    :return: отсортированный (или исходный) список строк.
    """
    if mode == "asc":
        return sorted(strings)
    elif mode == "desc":
        return sorted(strings, reverse=True)
    return strings


if __name__ == "__main__":
    args = parse_args()

    if args.test:
        args.strings = TEST_STRINGS
        args.unique = TEST_UNIQUE
        args.min_length = TEST_MIN_LENGTH
        args.sort = TEST_SORT
        args.count = TEST_COUNT

    if not args.strings:
        print(ERROR_NO_STRINGS, file=sys.stderr)
        sys.exit(1)

    filtered = filter_strings(args.strings, args.unique, args.min_length)
    result = sort_strings(filtered, args.sort)

    if args.count:
        print(len(result))
    else:
        for s in result:
            print(s)


