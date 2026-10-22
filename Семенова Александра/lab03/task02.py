#!/usr/bin/env python3

MIN_DISCOUNT = 0
MAX_DISCOUNT = 100
STOP_WORDS = ("стоп", "stop", "")

DEFAULT_PRODUCTS = [
    {"name": "Laptop",    "price": 89990, "discount": 10},
    {"name": "Mouse",     "price":  2490, "discount": 15},
    {"name": "Keyboard",  "price":  5490, "discount":  0},
    {"name": "Monitor",   "price": 27990, "discount": 25},
]


def ask_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ("да", "yes"):
            return True
        elif answer in ("нет", "no"):
            return False
        print("  Пожалуйста, введите 'да' или 'нет'.")


def read_positive_int(prompt, error_msg):
    while True:
        value_str = input(prompt).strip()
        try:
            value = int(value_str)
            if value < 0:
                print(f"   {error_msg} (число не может быть отрицательным).")
                continue
            return value
        except ValueError:
            print(f" {error_msg} (введите целое число).")


def read_discount():
    while True:
        value_str = input(f"Скидка в % ({MIN_DISCOUNT}–{MAX_DISCOUNT}): ").strip()
        try:
            value = int(value_str)
            if not (MIN_DISCOUNT <= value <= MAX_DISCOUNT):
                print(f"  Скидка должна быть от {MIN_DISCOUNT} до {MAX_DISCOUNT}.")
                continue
            return value
        except ValueError:
            print("  Неверный формат. Введите целое число.")


def input_products():
    products = []
    print("\nВведите 'стоп' в поле названия, чтобы закончить.\n")

    while True:
        name = input("Название товара: ").strip()
        if name.lower() in STOP_WORDS:
            break

        price = read_positive_int("Цена (целое число): ", "Цена не может быть отрицательной")
        discount = read_discount()

        products.append({"name": name, "price": price, "discount": discount})
        print()

    return products


def add_final_price(products):
    return list(map(
        lambda p: {**p, "final_price": p["price"] * (100 - p["discount"]) / 100},
        products
    ))


def merge(left, right, key_func):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(arr, key_func):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_func)
    right = merge_sort(arr[mid:], key_func)
    return merge(left, right, key_func)


def print_catalog(products):
    sorted_products = merge_sort(products, key=lambda p: p["final_price"])

    print(f"{'Название':<12} {'Цена':>8} {'Скидка':>7} {'Итог':>10}")
    for p in sorted_products:
        print(f"{p['name']:<12} {p['price']:>8} {p['discount']:>6}% "
              f"{p['final_price']:>10.2f}")


if __name__ == "__main__":
    want_custom = ask_yes_no("Хотите добавить свои товары? (да/нет): ")

    products = []
    if want_custom:
        products = input_products()
        
    if not products:
        print("Список пуст, использую значения по умолчанию.\n")
        products = DEFAULT_PRODUCTS

    products_with_final = add_final_price(products)
    print_catalog(products_with_final)

    input("\nНажмите Enter для выхода")

