#!/usr/bin/env python3

DEFAULT_PRODUCTS = [
    {"name": "Laptop",    "price": 89990, "discount": 10},
    {"name": "Mouse",     "price":  2490, "discount": 15},
    {"name": "Keyboard",  "price":  5490, "discount":  0},
    {"name": "Monitor",   "price": 27990, "discount": 25},
]

MIN_DISCOUNT = 0
MAX_DISCOUNT = 100
STOP_WORDS = ["стоп", "stop", ""]

def ask_yes_no(question):
    """
    Задаёт вопрос и принимает только 'да' или 'нет'.
    Переспрашивает, пока не получит корректный ответ.
    """
    while True:
        answer = input(question).strip().lower()
        if answer == "да" or answer == "yes":
            return True
        elif answer == "нет" or answer == "no":
            return False
        else:
            print("  Пожалуйста, введите 'да' или 'нет'.")

def read_positive_int(prompt, error_msg):
    """
    Запрашивает у пользователя целое неотрицательное число.

    Повторяет запрос, пока ввод не будет корректным.

    :Args: 
        prompt: текст приглашения ввода.
        error_msg: сообщение об ошибке при невалидном вводе.

    :Return:
        Введённое пользователем целое неотрицательное число.
    """
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
    """
    Запрашивает у пользователя размер скидки в процентах.

    :Returns:
        Целое число от 0 до 100 включительно.
    """
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
    """
    Интерактивно формирует список товаров со свойствами name, price, discount.

    Ввод завершается, когда пользователь вводит одно из слов-стопов в поле названия.

    :Returns:
        Список словарей вида {'name': str, 'price': int, 'discount': int}.
    """
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
    """
    Возвращает новый список словарей, в котором к каждому товару
    добавлено поле 'final_price' - цена с учётом скидки.

    Исходные словари не изменяются (создаются их копии через {**p, ...}).

    :Args:
        products: список словарей с ключами 'price' и 'discount'.

    :Returns:
        Новый список словарей с добавленным ключом 'final_price'.
    """
    return list(map(
        lambda p: {**p, "final_price": p["price"] * (100 - p["discount"]) / 100},
        products
    ))


def print_catalog(products):
    """
    Выводит каталог товаров в виде таблицы, отсортированной
    по возрастанию поля 'final_price'.

    :Args:
        products: список словарей с ключами 'name', 'price',
                  'discount', 'final_price'.
    """
    sorted_products = sorted(products, key=lambda p: p["final_price"])

    print(f"{'Название':<12} {'Цена':>8} {'Скидка':>7} {'Итог':>10}")
    for p in sorted_products:
        print(f"{p['name']:<12} {p['price']:>8} {p['discount']:>6}% "
              f"{p['final_price']:>10.2f}")


if __name__ == "__main__":

    want_custom = ask_yes_no("Хотите добавить свои товары? (да/нет): ")

    if want_custom:
        products = input_products()
    else:
        products = []

    if not products:
        print("Список пуст, использую значения по умолчанию.\n")
        products = DEFAULT_PRODUCTS

    products_with_final = add_final_price(products)
    print_catalog(products_with_final)
    