#!/usr/bin/env python3

from functools import reduce

MIN_WORD_LENGTH = 7
STOP_WORDS = ["стоп"]

def is_number(token):
    """
    Проверяет, является ли строка числом (целым или дробным,
    возможно отрицательным).

    :Args:
        token: строка для проверки.

    :Returns:
        True, если строка является числом; False в противном случае.
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def get_words_from_user():
    """
    Получает от пользователя список слов.

    Числа из ввода игнорируются с выводом предупреждения.
    Переспрашивает, пока пользователь не введёт хотя бы одно слово
    или не введёт слово-стоп.

    :Returns:
        Список строк (только слова, без чисел).
    """
    while True:
        raw = input("Введите слова через пробел. Для завершения напишите 'стоп', чтобы завершить ввод - нажмите Enter: ").strip()

        if raw.lower() in STOP_WORDS:
            print("Ввод отменён.")
            return []
        if not raw:
            if words:
                print("Ввод завершён.")
                return words

        tokens = raw.split()

        if not tokens:
            print("Вы ничего не ввели. Пожалуйста, введите хотя бы одно слово.")
            continue

        words = []
        for token in tokens:
            if is_number(token):
                print(f"'{token}' - это число, а не слово. Вводите слова.")
            else:
                words.append(token)

def filter_long_words(words, min_length):
    """
    Оставляет только слова длиной не менее min_length символов.

    :Args:
        words: список строк.
        min_length: минимальная длина слова.

    :Returns:
        Новый список слов, удовлетворяющих условию.
    """
    return list(filter(lambda word: len(word) >= min_length, words))


def make_word_length_pairs(words):
    """
    Преобразует каждое слово в пару (слово, длина).

    :Args:
        words: список строк.

    :Returns:
        Список кортежей вида (слово, длина).
    """
    return list(map(lambda word: (word, len(word)), words))


def find_longest_word(pairs):
    """
    Находит пару (слово, длина) с максимальной длиной.

    :Args:
        pairs: список кортежей (слово, длина).

    :Returns:
        Кортеж (слово, длина) с максимальной длиной.
    """
    return reduce(
        lambda max_pair, current_pair: current_pair if current_pair[1] > max_pair[1] else max_pair,
        pairs
    )


def count_total_letters(pairs):
    """
    Считает суммарное количество букв во всех словах.

    :Args:
        pairs: список кортежей (слово, длина).

    :Returns:
        Сумма длин всех слов.
    """
    return reduce(lambda total, pair: total + pair[1], pairs, 0)


if __name__ == "__main__":

    words = get_words_from_user()

    if not words:
        print("Программа завершена.")
    else:
        print(f"\nИсходный список ({len(words)} слов):")
        print(words)
    
        filtered_words = filter_long_words(words, MIN_WORD_LENGTH)
        print(f"После фильтрации (длина >= {MIN_WORD_LENGTH}):")
        print(f"Количество слов: {len(filtered_words)}")
        print(f"Слова: {filtered_words}")
   

        word_length_pairs = make_word_length_pairs(filtered_words)

        if word_length_pairs:
            print("Пары (слово, длина):")
            for pair in word_length_pairs:
                print(f"  {pair[0]:<15} → {pair[1]}")
         

            longest_pair = find_longest_word(word_length_pairs)
            print(f"Слово с максимальной длиной:")
            print(f"'{longest_pair[0]}' — {longest_pair[1]} символов")
     
            total_letters = count_total_letters(word_length_pairs)
            print(f"Суммарное количество букв: {total_letters}")
        else:
            print("Нет слов, удовлетворяющих условию (длина >= 7).")
            