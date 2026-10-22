#!/usr/bin/env python3

from functools import reduce

MIN_WORD_LENGTH = 7
STOP_WORDS = ("стоп", "stop", "")


def is_number(token):
    """
    Проверяет, является ли строка целым числом.
    Дробные числа и буквы возвращают False.
    """
    cleaned = token.lstrip('-')
    return bool(cleaned) and cleaned.isdigit()


def get_words_from_user():
    """
    Получает от пользователя список слов.
    Числа игнорируются с предупреждением.
    Завершается по пустому вводу (Enter), отменяется по 'стоп'.
    """
    print("Введите слова через пробел.")
    print("Нажмите Enter для завершения.\n")
    
    words = []  # Инициализируем список ДО цикла, чтобы избежать ошибки
    
    while True:
        raw = input("Ввод: ").strip()

        if raw.lower() in ("стоп", "stop"):
            print("Ввод отменён.")
            return []
        
        if not raw:
            if words:
                print("Ввод завершён.")
            return words

        tokens = raw.split()
        
        if not tokens:
            continue

        for token in tokens:
            if is_number(token):
                print(f"'{token}' - это число, а не слово. Пропускаем.")
            else:
                words.append(token)


def filter_long_words(words, min_length):
    return list(filter(lambda word: len(word) >= min_length, words))


def make_word_length_pairs(words):
    return list(map(lambda word: (word, len(word)), words))


def find_longest_word(pairs):
    return reduce(
        lambda max_pair, current_pair: current_pair if current_pair[1] > max_pair[1] else max_pair,
        pairs
    )


def count_total_letters(pairs):
    return reduce(lambda total, pair: total + pair[1], pairs, 0)


if __name__ == "__main__":
    
    words = get_words_from_user()

    if not words:
        print("Программа завершена.")
        exit()

    print(f"\nИсходный список ({len(words)} слов):")
    print(words)

    filtered_words = filter_long_words(words, MIN_WORD_LENGTH)
    print(f"\nПосле фильтрации (длина >= {MIN_WORD_LENGTH}):")
    print(f"Количество слов: {len(filtered_words)}")

    if filtered_words:
        print(f"Слова: {filtered_words}")

        word_length_pairs = make_word_length_pairs(filtered_words)
        print("\nПары (слово, длина):")

        for pair in word_length_pairs:
            print(f"  {pair[0]:<15} → {pair[1]}")

        longest_pair = find_longest_word(word_length_pairs)
        print(f"\nСлово с максимальной длиной:")
        print(f"  '{longest_pair[0]}' — {longest_pair[1]} символов")

        total_letters = count_total_letters(word_length_pairs)
        print(f"Суммарное количество букв: {total_letters}")
    else:
        print("Нет слов, удовлетворяющих условию (длина >= 7).")
