#!/usr/bin/env python3

SORT_ASCENDING = "1"
SORT_DESCENDING = "2"
VALID_CHOICES = (SORT_ASCENDING, SORT_DESCENDING)

def get_numbers():
   
    print("Введите числа (пустой ввод для завершения)")
    numbers = []

    while True:
        text = input("Число(чтобы выйти нажмите Enter): ")
        if text == "":
            break
        try:
            number = float(text)
            numbers.append(number)
        except ValueError:
            print("Ошибка: введите число! Попробуйте снова.\n")

    return numbers

def get_sort_order():
    
    print("\nВыберите порядок сортировки:")
    print("1 - По возрастанию")
    print("2 - По убыванию")

    while True:
        choice = input("Ваш выбор: ")
        if choice in VALID_CHOICES:
            return choice
        print("Ошибка: введите 1 или 2!")

def sort_numbers(numbers, order):
    
    if order == SORT_ASCENDING:
        return sorted(numbers)
    else:
        return sorted(numbers, reverse=True)

def get_order_name(order):
    
    if order == SORT_ASCENDING:
        return "возрастанию"
    else:
        return "убыванию"

if __name__ == "__main__":
    try:
        numbers = get_numbers()

        if not numbers:
            print("Список чисел пуст!")
        else:
            order = get_sort_order()
            result = sort_numbers(numbers, order)
            order_name = get_order_name(order)

            print(f"\nЧисла по {order_name}: {result}")
