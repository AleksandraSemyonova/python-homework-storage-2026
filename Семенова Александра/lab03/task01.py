#!/usr/bin/env python3

def classify(n):
    """
    Классифицирует целое число по знаку и чётности.

    :Args: n: целое число для классификации.

    :Return: 
        Строка с описанием категории числа:
        - 'positive even' - положительное чётное;
        - 'positive odd'  - положительное нечётное;
        - 'negative'      - отрицательное;
        - 'zero'          - ноль.
    """
    if n > 0 and n % 2 == 0:
        return "positive even"
    elif n > 0 and n % 2 != 0:
        return "positive odd"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def read_integers():
    """
    Считывает строку от пользователя и возвращает список целых чисел.

    Невалидные символы (буквы, дробные числа) пропускаются с выводом
    предупреждения в консоль.

    :Return:
        Список целых чисел, успешно распознанных во вводе.
    """
    raw = input("Введите целые числа через пробел: ").split()
    numbers = []
    for item in raw:
        try:
            numbers.append(int(item))
        except ValueError:
            print(f"'{item}' - не целое число, пропускаем.")
    return numbers


if __name__ == "__main__":

    numbers = read_integers()

    if not numbers:
        print("Вы не ввели ни одного корректного числа.")
    else:
        print("\nРезультат:")
        
        for n in numbers:
            print(f"{n:>6} : {classify(n)}")
            