#!/usr/bin/env python3

VOWELS = ('а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я','a', 'e', 'i', 'o', 'u')

MIN_VOWELS = 3
EMPTY_DICT = ()

def count_vowels(text):
    count = 0
    text_lower = text.lower()
    for symbol in VOWELS:
        if symbol in VOWELS:      
            count += 1
    return count

def filter_kwargs(**kwargs):
    result = {}

    for (key, value) in kwargs.items():
        if type(value) == str:
            vowels_count = count_vowels(value)
            if vowels_count >= MIN_VOWELS:
                result[key] = value
    return result

def get_yes_no(prompt):
    while True:
        answer = input(prompt).lower()
        if answer in ('да', 'нет'):
            return answer
        print("Ошибка: введите 'да' или 'нет'!")

def get_kwargs_from_user():
    print("Введите аргументы (формат: имя=значение).")
    print("Пустой ввод имени — завершение.")

    kwargs = {}

    while True:
        key = input("Имя аргумента: ")
        if key.strip() == "":
            if not kwargs:
                print("Ошибка: нужно ввести хотя бы один аргумент!")
            else:
                break

        value = input("Значение: ")
        kwargs[key] = value

        again = get_yes_no("Добавить ещё аргумент? (да/нет): ")
        if again == 'нет':
            break

    return kwargs

def print_result(result):
    if not result:
        print("Аргументы со строками, содержащими 3 и более гласных, не найдены.")
    else:
        print("Найденные аргументы:")
        for key, value in result.items():
            print(f"  {key} = {value}")


if __name__ == "__main__":
    try:
        start = get_yes_no("Хотите ввести аргументы? (да/нет): ")

        if start == 'нет':
            print("Программа завершена. Аргументы не были введены.")
        else:
            kwargs = get_kwargs_from_user()
            result = filter_kwargs(**kwargs)
            print_result(result)

    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")
        print("Попробуйте запустить программу снова.")
