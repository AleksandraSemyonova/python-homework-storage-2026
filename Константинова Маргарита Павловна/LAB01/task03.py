#!/usr/bin/env python3

import string

GLASNYE = "аеёиоуыэюя"
SOGLASNYE = "бвгджзйклмнопрстфхцчшщъь"


def main():
    stroka = input("Введите слова через пробел: ")
    slova = tuple(stroka.split())

    print(f"Кортеж слов: {slova}")
    print(f"Уникальных слов: {len(set(slova))}")

    nizhniy_registr = stroka.lower()
    glasnye = sum(1 for s in nizhniy_registr if s in GLASNYE)
    soglasnye = sum(1 for s in nizhniy_registr if s in SOGLASNYE)
    znaki = sum(1 for s in stroka if s in string.punctuation)

    print(f"Гласных: {glasnye}")
    print(f"Согласных: {soglasnye}")
    print(f"Знаков препинания: {znaki}")


if __name__ == "__main__":
    main()
