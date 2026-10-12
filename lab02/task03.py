#!/usr/bin/env python3

TRUE_VALUES = ("True", "true", "1")
FALSE_VALUES = ("False", "false", "0")


def parse_value(text):
    """Пытается определить тип введённого значения."""
    text = text.strip()

    # Проверка на булево (до int, т.к. bool — подтип int)
    if text in TRUE_VALUES or text in FALSE_VALUES:
        if text in TRUE_VALUES:
            return True
        else:
            return False

    # Проверка на целое число
    try:
        return int(text)
    except ValueError:
        pass

    # Проверка на дробное число
    try:
        return float(text)
    except ValueError:
        pass

    # Иначе — строка
    return text


def get_yes_no(prompt):
    """Запрашивает ответ 'да' или 'нет' с проверкой."""
    while True:
        answer = input(prompt).lower()
        if answer in ('да', 'нет'):
            return answer
        print("Ошибка: введите 'да' или 'нет'!")


def get_arguments():
    """Запрашивает у пользователя аргументы разных типов."""
    print("Введите аргументы через пробел (пустой ввод для завершения)")
    arguments = []

    while True:
        text = input("Аргумент: ")
        if text.strip() == "":
            if not arguments:
                print("Ошибка: нужно ввести хотя бы один аргумент!")
                continue
            else:
                break

        parts = text.split(" ")
        for part in parts:
            if part.strip() != "":
                value = parse_value(part)
                arguments.append(value)

        again = get_yes_no("Добавить ещё аргументы? (да/нет): ")
        if again == 'нет':
            break

    return arguments


def multiply_integers(arguments):
    """
    Возвращает произведение целочисленных аргументов.
    Если целых нет — возвращает список нецелых с их типами.
    """
    product = 1
    has_integer = False
    non_integers = []

    for arg in arguments:
        if type(arg) is int:
            product = product * arg
            has_integer = True
        else:
            non_integers.append((arg, type(arg)))

    if has_integer:
        return product
    else:
        return non_integers


def print_result(result):
    """Выводит результат работы программы."""
    if type(result) is int:
        print("Произведение целочисленных аргументов:", result)
    else:
        print("Целочисленные аргументы не были поданы.")
        print("Нецелые значения и их типы:")
        for pair in result:
            value = pair[0]
            arg_type = pair[1]
            print(f"  Значение: {value} | Тип: {arg_type}")


if __name__ == "__main__":
    try:
        # Спрашиваем, хочет ли пользователь начать
        start = get_yes_no("Хотите ввести аргументы? (да/нет): ")

        if start == 'нет':
            print("Программа завершена. Аргументы не были введены.")
        else:
            arguments = get_arguments()
            result = multiply_integers(arguments)
            print_result(result)

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        print("Попробуйте запустить программу снова.")
