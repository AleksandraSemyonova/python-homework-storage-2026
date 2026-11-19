#!/usr/bin/env python3

import argparse
import random
import string
import sys
import os


ERROR_LENGTH_RANGE = "Длина пароля должна быть от 8 до 64 символов."
ERROR_COUNT_POSITIVE = "Количество паролей должно быть положительным числом."
ERROR_NO_SYMBOLS = "Невозможно сгенерировать пароль: пул символов пуст после исключений."
ERROR_FILE_EXISTS = "Файл уже существует. Используйте --force для перезаписи."

MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 64
MIN_PASSWORD_COUNT = 1

def parse_args():
    """
    Парсит аргументы командной строки.

    :return: Аргументы:
        length (int): длина пароля (от 8 до 64);
        count (int): количество паролей для генерации;
        no_digits (bool): если True, исключить цифры;
        no_special (bool): если True, исключить специальные символы;
        output (str или None): путь к файлу для сохранения паролей;
        force (bool): если True, разрешить перезапись файла;
        test (bool): если True, запустить с тестовыми значениями.
    """
    parser = argparse.ArgumentParser(description="Генератор паролей")

    parser.add_argument(
        "--length",
        type=int,
        required=True,
        help="Длина пароля (от 8 до 64)",
    )
    parser.add_argument(
        "--count",
        type=int,
        required=True,
        help="Количество паролей для генерации",
    )
    parser.add_argument(
        "--no-digits",
        action="store_true",
        help="Исключить цифры из пароля",
    )
    parser.add_argument(
        "--no-special",
        action="store_true",
        help="Исключить специальные символы из пароля",
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Файл для сохранения паролей",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Разрешить перезапись существующего файла",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Запустить с тестовыми значениями",
    )
    return parser.parse_args()


def get_symbol_pool(no_digits, no_special):
    """
    Формирует пул символов для генерации пароля.

    :param no_digits: если True, исключить цифры.
    :param no_special: если True, исключить специальные символы.
    :return: строка с доступными символами.
    """
    pool = string.ascii_letters  #всегда включаем буквы
    
    if not no_digits:
        pool += string.digits
    
    if not no_special:
        pool += string.punctuation
    
    return pool


def generate_password(length, pool):
    """
    Генерирует пароль заданной длины из пула символов.

    :param length: длина пароля.
    :param pool: строка с доступными символами.
    :return: сгенерированный пароль.
    """
    return ''.join(random.choice(pool) for _ in range(length))


if __name__ == "__main__":
    args = parse_args()

    if args.length < MIN_PASSWORD_LENGTH or args.length > MAX_PASSWORD_LENGTH:
        raise ValueError(ERROR_LENGTH_RANGE)

    if args.count <= MIN_PASSWORD_COUNT:
        raise ValueError(ERROR_COUNT_POSITIVE)

    pool = get_symbol_pool(args.no_digits, args.no_special)

    if not pool:
        raise ValueError(ERROR_NO_SYMBOLS)      

    if args.output and os.path.exists(args.output) and not args.force:
        raise ValueError(ERROR_FILE_EXISTS)

    passwords = [generate_password(args.length, pool) for _ in range(args.count)]

    print(f"Сгенерировано {args.count} пароль(ей) длиной {args.length} символов:\n")
    for i, pwd in enumerate(passwords, 1):
        print(f"{i}. {pwd}")

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f"\n Пароли сохранены в файл: {args.output}")

