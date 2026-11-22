#!/usr/bin/env python3

import argparse
import random
import string


MIN_LENGTH = 8
MAX_LENGTH = 64
DEFAULT_LENGTH = 16
DEFAULT_COUNT = 1
MIN_COUNT = 1
MAX_COUNT = 100

ERROR_LENGTH_RANGE = (
    f"Длина пароля должна быть от {MIN_LENGTH} до {MAX_LENGTH} символов."
)
ERROR_COUNT_RANGE = (
    f"Количество паролей должно быть от {MIN_COUNT} до {MAX_COUNT}."
)


def generate_password(length=DEFAULT_LENGTH, use_digits=True,
                      use_upper=True, use_special=False):
    """
    Генерирует случайный пароль заданной длины.

    Args:
        length: длина пароля.
        use_digits: включать ли цифры.
        use_upper: включать ли заглавные буквы.
        use_special: включать ли спецсимволы.

    Returns:
        str: сгенерированный пароль.
    """
    pool = string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_upper:
        pool += string.ascii_uppercase
    if use_special:
        pool += string.punctuation

    return ''.join(random.choice(pool) for _ in range(length))


def validate_length(length):
    """
    Проверяет корректность длины пароля.

    Args:
        length: длина пароля.

    Returns:
        bool: True, если длина корректна.

    Raises:
        ValueError: если длина вне допустимого диапазона.
    """
    if not (MIN_LENGTH <= length <= MAX_LENGTH):
        raise ValueError(ERROR_LENGTH_RANGE)
    return True


def validate_count(count):
    """
    Проверяет корректность количества паролей.

    Args:
        count: количество паролей.

    Returns:
        bool: True, если количество корректно.

    Raises:
        ValueError: если количество вне допустимого диапазона.
    """
    if not (MIN_COUNT <= count <= MAX_COUNT):
        raise ValueError(ERROR_COUNT_RANGE)
    return True


def parse_args(argv=None):
    """
    Разбирает аргументы командной строки.

    Args:
        argv: список аргументов.

    Returns:
        argparse.Namespace: пространство имён с полями length, count,
            no-digits, no-upper, special.
    """
    parser = argparse.ArgumentParser(
        description="Генератор случайных паролей."
    )
    parser.add_argument(
        "--length", type=int, default=DEFAULT_LENGTH,
        help=f"Длина пароля (по умолчанию {DEFAULT_LENGTH})."
    )
    parser.add_argument(
        "--count", type=int, default=DEFAULT_COUNT,
        help=f"Количество паролей (по умолчанию {DEFAULT_COUNT})."
    )
    parser.add_argument(
        "--no-digits", action="store_true",
        help="Не включать цифры."
    )
    parser.add_argument(
        "--no-upper", action="store_true",
        help="Не включать заглавные буквы."
    )
    parser.add_argument(
        "--special", action="store_true",
        help="Включить спецсимволы."
    )
    return parser.parse_args(argv)


def run(length=DEFAULT_LENGTH, count=DEFAULT_COUNT,
        no_digits=False, no_upper=False, special=False):
    """
    Генерирует и выводит пароли.

    Args:
        length: длина пароля.
        count: количество паролей.
        no_digits: не включать цифры.
        no_upper: не включать заглавные буквы.
        special: включать спецсимволы.
    """
    validate_length(length)
    validate_count(count)

    use_digits = not no_digits
    use_upper = not no_upper

    for _ in range(count):
        password = generate_password(
            length=length,
            use_digits=use_digits,
            use_upper=use_upper,
            use_special=special,
        )
        print(password)


if __name__ == "__main__":
    args = parse_args()


    run(
            length=args.length,
            count=args.count,
            no_digits=args.no_digits,
            no_upper=args.no_upper,
            special=args.special,
        )

