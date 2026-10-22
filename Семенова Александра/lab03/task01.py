#!/usr/bin/env python3

classify = lambda n: "positive even" if n > 0 and n % 2 == 0 else "positive odd" if n > 0 else "negative" if n < 0 else "zero"


def read_integers():
    """
     :param user_input: Считывает целые числа, введённые пользователем через пробел.

    Ввод можно повторять несколько раз. Пустая строка (нажатие Enter)
    завершает ввод и возвращает все собранные числа.
    Некорректные значения пропускаются с выводом предупреждения.

    :return: Список успешно распознанных целых чисел. Если корректных чисел нет - пустой список.
    """
    print("Введите целые числа через пробел.")
    print("Enter - завершить ввод.\n")

    numbers = []

    while True:
        raw = input("Числа: ")

        if not raw.strip():
            break

        for item in raw.split():
            try:
                numbers.append(int(item))
            except ValueError:
                print(f"'{item}' - не целое число, пропускаем. Вводите только числа.")

    return numbers


if __name__ == "__main__":
    numbers = read_integers()

    if not numbers:
        print("Вы не ввели ни одного корректного числа.")
    else:
        print("\nРезультат:")
        for n in numbers:
            print(f"{n:>6} : {classify(n)}")
       
