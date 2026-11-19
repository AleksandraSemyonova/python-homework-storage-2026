#!/usr/bin/env python3

import argparse
import os

MAX_SPLITS = 1

def parse_replace(arg):
    """
    Парсит аргумент --replace в формате OLD=NEW.

    :param arg: строка в формате OLD=NEW.
    :return: кортеж (OLD, NEW).
    :raises ValueError: если формат неверный или OLD пустой.
    """
    if '=' not in arg:
        raise ValueError(f"Неверный формат замены: '{arg}'. Ожидается OLD=NEW.")
    parts = arg.split('=', MAX_SPLITS)
    old, new = parts[0], parts[1]
    if not old:
        raise ValueError("Строка OLD не может быть пустой.")
    return old, new


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Утилита для копирования файлов с заменой текста и добавлением подвала."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Путь к входному файлу.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Путь к выходному файлу.",
    )
    parser.add_argument(
        "--replace",
        action="append",
        default=[],
        help="Замена в формате OLD=NEW. Можно указывать несколько раз.",
    )
    parser.add_argument(
        "--append-footer",
        default=None,
        help="Строка, которую нужно добавить в конец выходного файла.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Разрешить перезапись существующего выходного файла.",
    )

    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise f"Входной файл не существует: {args.input}"

    if os.path.exists(args.output) and not args.force:
        raise f"Выходной файл уже существует: {args.output}. "f"Используйте --force для перезаписи."
        

    with open(args.input, 'r', encoding='utf-8-sig') as f:
        content = f.read()

    total_replacements = 0
    for replace_arg in args.replace:
        old, new = parse_replace(replace_arg)
        count = content.count(old)
        content = content.replace(old, new)
        total_replacements += count
        print(f"Заменено '{old}' на '{new}': {count} раз.")

    if args.append_footer is not None:
        if content and not content.endswith('\n'):
            content += '\n'              #чтобы начиналось с новой строки
        content += args.append_footer
        if not content.endswith('\n'):
            content += '\n'

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nВсего выполнено замен: {total_replacements}")
    print(f"Результат записан в: {args.output}")

