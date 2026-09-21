#!/usr/bin/env python3


def vse_razlichny(chisla):
    return len(chisla) == len(set(chisla))


def main():
    chisla = [float(x) for x in input("Введите числа через пробел: ").split()]

    if vse_razlichny(chisla):
        print("Все числа различны.")
    else:
        print("Среди чисел есть повторяющиеся значения.")


if __name__ == "__main__":
    main()
