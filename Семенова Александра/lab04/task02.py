#!/usr/bin/env python3

MAX_WITHDRAW_PERCENT = 0.5  
INTEREST_DIVISOR = 100      
TEST_WITHDRAW_AMOUNT = 100 
TEST_BIG_WITHDRAW_PERCENT = 0.6  


class BankAccount:
    """
    Базовый класс банковского счёта.

    Хранит владельца, баланс и историю операций.
    Поля объявлены как protected, так как наследники
    обращаются к ним через свойства и методы.
    """

    def __init__(self, owner, initial_balance=0):
        """
        Инициализирует банковский счёт.

        :param owner: имя владельца счёта (непустая строка).
        :param initial_balance: начальный баланс (неотрицательное число).
        :raises ValueError: если owner или initial_balance невалидны.
        """
        self._owner = None
        self._balance = 0
        self._history = []
        self.owner = owner
        if initial_balance > 0:
            self.deposit(initial_balance)

    @property
    def owner(self):
        """Возвращает имя владельца счёта."""
        return self._owner

    @owner.setter
    def owner(self, value):
        """
        Устанавливает имя владельца с валидацией.

        :param value: новое имя владельца.
        :raises ValueError: если value не строка или пустая.
        """
        if type(value) is not str or not value.strip():
            raise ValueError("Имя владельца должно быть непустой строкой.")
        self._owner = value

    @property
    def balance(self):
        """Возвращает текущий баланс счёта."""
        return self._balance

    @property
    def history(self):
        """Возвращает копию истории операций."""
        return self._history.copy()

    def deposit(self, amount):
        """
        Пополняет счёт на указанную сумму.

        :param amount: сумма пополнения (положительное число).
        :return: True, если операция успешна; False, если amount невалиден.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print("Ошибка: сумма пополнения должна быть положительным числом.")
            return False

        self._balance += amount
        self._history.append(f"Пополнение: +{amount}. Баланс: {self._balance}")
        return True

    def withdraw(self, amount):
        """
        Снимает указанную сумму со счёта.

        :param amount: сумма снятия (положительное число).
        :return: True, если операция успешна; False, если amount невалиден или недостаточно средств.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print("Ошибка: сумма снятия должна быть положительным числом.")
            return False

        if amount > self._balance:
            print(f"Ошибка: недостаточно средств. Баланс: {self._balance}.")
            return False

        self._balance -= amount
        self._history.append(f"Снятие: -{amount}. Баланс: {self._balance}")
        return True

    @classmethod
    def from_dict(cls, data):
        """
        Создаёт объект счёта из словаря.

        Значения читаются через .get(), чтобы при отсутствии ключа
        не возникал KeyError, а понятная ValueError.

        :param data: словарь с ключами 'owner' и 'balance'.
        :return: новый объект BankAccount.
        :raises ValueError: если ключ 'owner' отсутствует.
        """
        owner = data.get("owner")
        balance = data.get("balance", 0)
        if owner is None:
            raise ValueError("В словаре отсутствует ключ 'owner'.")
        return cls(owner=owner, initial_balance=balance)

    def __str__(self):
        """
        Возвращает строковое представление счёта.

        Магический метод __str__ автоматически вызывается print(obj)
        и str(obj), поэтому его используют вместо кастомных методов.

        :return: строка с описанием счёта.
        """
        return f"Владелец: {self._owner}, Баланс: {self._balance}"


class SavingsAccount(BankAccount):
    """
    Класс сберегательного счёта, наследующий BankAccount.

    Добавляет процентную ставку и ограничение на снятие.
    Поле rate объявлено как private, так как оно уникально
    для этого класса и не используется другими наследниками.
    """

    def __init__(self, owner, initial_balance=0, rate=0):
        """
        Инициализирует сберегательный счёт.

        :param owner: имя владельца счёта.
        :param initial_balance: начальный баланс.
        :param rate: процентная ставка в процентах (неотрицательное число).
        :raises ValueError: если owner или rate невалидны.
        """
        super().__init__(owner, initial_balance)
        self.__rate = None
        self.rate = rate

    @property
    def rate(self):
        """Возвращает процентную ставку."""
        return self.__rate

    @rate.setter
    def rate(self, value):
        """
        Устанавливает процентную ставку с валидацией.

        :param value: новое значение ставки.
        :raises ValueError: если value не число или отрицательное.
        """
        if type(value) not in (int, float) or value < 0:
            raise ValueError("Процентная ставка должна быть неотрицательным числом.")
        self.__rate = value

    def add_interest(self):
        """
        Начисляет проценты на текущий баланс.

        :return: сумма начисленных процентов.
        """
        interest = self._balance * self.__rate / INTEREST_DIVISOR
        if interest > 0:
            self.deposit(interest)
        return interest

    def withdraw(self, amount):
        """
        Снимает сумму со счёта (не более 50% баланса за одну операцию).

        :param amount: сумма снятия (положительное число).
        :return: True, если операция успешна; False, если amount невалиден,
                 превышает 50% баланса или недостаточно средств.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print("Ошибка: сумма снятия должна быть положительным числом.")
            return False

        max_withdraw = self._balance * MAX_WITHDRAW_PERCENT
        if amount > max_withdraw:
            print(
                f"Ошибка: со сберегательного счёта нельзя снять более "
                f"{MAX_WITHDRAW_PERCENT * 100}% баланса ({max_withdraw})."
            )
            return False

        if amount > self._balance:
            print(f"Ошибка: недостаточно средств. Баланс: {self._balance}.")
            return False

        self._balance -= amount
        self._history.append(f"Снятие (Сбер): -{amount}. Баланс: {self._balance}")
        return True

    def __str__(self):
        """
        Возвращает строковое представление сберегательного счёта.

        :return: строка с описанием счёта.
        """
        return f"{super().__str__()}, Ставка: {self.__rate}%"


if __name__ == "__main__":
    print("=== 1. Создание объектов ===")
    account = BankAccount("Иван", 1500)
    savings = SavingsAccount("Мария", 6000, rate=5)
    account2 = BankAccount("Пётр", 2500)

    print(account)
    print(savings)
    print(account2)

    print("\n=== 2. Корректное пополнение и снятие ===")
    account.deposit(500)
    account.withdraw(200)
    print(f"Баланс {account.owner}: {account.balance}")

    savings.deposit(1000)
    savings.withdraw(500)
    print(f"Баланс {savings.owner}: {savings.balance}")

    print("\n=== 3. Ошибки: отрицательная сумма и превышение баланса ===")
    account.deposit(-100)
    account.withdraw(-50)
    account.withdraw(100000)

    print("\n=== 4. Невозможность изменить баланс напрямую ===")
    try:
        account.balance = 999999
    except AttributeError as e:
        print(f"Ошибка: {e}")

    print(f"Баланс остался: {account.balance}")

    print("\n=== 5. Вывод истории операций ===")
    print(f"История {account.owner}:")
    for entry in account.history:
        print(f"  {entry}")

    print(f"\nИстория {savings.owner}:")
    for entry in savings.history:
        print(f"  {entry}")

    print("\n=== 6. Начисление процентов на сберегательный счёт ===")
    print(f"Баланс до начисления: {savings.balance}")
    interest = savings.add_interest()
    print(f"Начислено процентов: {interest}")
    print(f"Баланс после начисления: {savings.balance}")

    print("\n=== 7. Полиморфное поведение метода снятия ===")
    accounts = (account, savings)

    for acc in accounts:
        print(f"\n{type(acc).__name__} ({acc.owner}), баланс: {acc.balance}")
        acc.withdraw(TEST_WITHDRAW_AMOUNT)
        print(f"После снятия {TEST_WITHDRAW_AMOUNT}: {acc.balance}")

    print("\n=== 8. Попытка снять более 50% со сберегательного счёта ===")
    print(f"Баланс {savings.owner}: {savings.balance}")
    big_amount = savings.balance * TEST_BIG_WITHDRAW_PERCENT
    savings.withdraw(big_amount)

    print("\n=== 9. Проверка, что history возвращает копию ===")
    history_copy = account.history
    history_copy.append("Попытка подменить историю")
    print(f"Реальная история: {account.history}")
    print("Копия не изменила внутренний список — защита работает.")

