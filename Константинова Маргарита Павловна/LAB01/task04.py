#!/usr/bin/env python3

ALFAVIT = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def main():
    vybor = input("1 - текст в числа, 2 - числа в текст: ")

    if vybor == "1":
        tekst = input("Введите текст: ").lower()
        chisla = [ALFAVIT.index(s) + 1 if s in ALFAVIT else 0 for s in tekst]
        print(*chisla)
    else:
        chisla = [int(x) for x in input("Введите числа через пробел: ").split()]
        tekst = "".join(ALFAVIT[n - 1] if n > 0 else " " for n in chisla)
        print(tekst)


if __name__ == "__main__":
    main()
