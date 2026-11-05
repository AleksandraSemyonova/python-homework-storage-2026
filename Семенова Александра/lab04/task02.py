#!/usr/bin/env python3

class BankAccount:
    """
    Класс банковского счёта.

    :param owner: имя владельца счёта.
    :param initial_balance: начальный баланс.
    """

    def __init__(self, owner, initial_balance=0):
        self.__owner = owner
        self.__balance = 0
        self.__history = []
        if initial_balance > 0:
            self.deposit(initial_balance)

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return self.__history.copy()

    def deposit(self, amount):
        """
        Пополняет счёт на указанную сумму.

        :param amount: сумма пополнения.
        :return: True, если операция успешна; False в противном случае.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print(f"Ошибка: сумма пополнения должна быть положительным числом.")
            return False

        self.__balance += amount
        self.__history.append(f"Пополнение: +{amount}. Баланс: {self.__balance}")
        return True

    def withdraw(self, amount):
        """
        Снимает указанную сумму со счёта.

        :param amount: сумма снятия.
        :return: True, если операция успешна; False в противном случае.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print(f"Ошибка: сумма снятия должна быть положительным числом.")
            return False

        if amount > self.__balance:
            print(f"Ошибка: недостаточно средств. Баланс: {self.__balance}.")
            return False

        self.__balance -= amount
        self.__history.append(f"Снятие(Тинькофф): -{amount}. Баланс: {self.__balance}")
        return True

    @classmethod
    def from_owner(cls, owner, initial_balance=0):
        """
        Создаёт объект счёта по имени владельца.

        :param owner: имя владельца.
        :param initial_balance: начальный баланс.
        :return: новый объект BankAccount.
        """
        return cls(owner=owner, initial_balance=initial_balance)


class SavingsAccount(BankAccount):
    """
    Класс сберегательного счёта, наследующий BankAccount.

    :param owner: имя владельца счёта.
    :param initial_balance: начальный баланс.
    :param rate: процентная ставка в процентах.
    """

    def __init__(self, owner, initial_balance=0, rate=0):
        super().__init__(owner, initial_balance)
        self.__rate = rate

    @property
    def rate(self):
        return self.__rate

    def add_interest(self):
        """
        Начисляет проценты на текущий баланс.

        :return: сумма начисленных процентов.
        """
        interest = self.balance * self.__rate / 100
        if interest > 0:
            self.deposit(interest)
            self._BankAccount__history.append(f"Начисление процентов: +{interest}. Баланс: {self.balance}")
        return interest

    def withdraw(self, amount):
        """
        Снимает сумму со счёта (не более 50% баланса за одну операцию).

        :param amount: сумма снятия.
        :return: True, если операция успешна; False в противном случае.
        """
        if type(amount) not in (int, float) or amount <= 0:
            print(f"Ошибка: сумма снятия должна быть положительным числом.")
            return False

        if amount > self.balance * 0.5:
            print(
                f"Ошибка: со сберегательного счёта нельзя снять более 50% "
                f"баланса ({self.balance * 0.5})."
            )
            return False

        if amount > self.balance:
            print(f"Ошибка: недостаточно средств. Баланс: {self.balance}.")
            return False

        self._BankAccount__balance -= amount
        self._BankAccount__history.append(f"Снятие (Сбер): -{amount}. Баланс: {self.balance}")
        return True


if __name__ == "__main__":
    print("=== 1. Создание объектов ===")
    account = BankAccount("Иван", 1500)
    savings = SavingsAccount("Мария", 6000, rate=5)
    account2 = BankAccount.from_owner("Пётр", 2500)

    print(f"{account.owner}: баланс {account.balance}")
    print(f"{savings.owner}: баланс {savings.balance}, ставка {savings.rate}%")
    print(f"{account2.owner}: баланс {account2.balance}")

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
        print(f"{entry}")

    print(f"\nИстория {savings.owner}:")
    for entry in savings.history:
        print(f"{entry}")

    print("\n=== 6. Начисление процентов на сберегательный счёт ===")
    print(f"Баланс до начисления: {savings.balance}")
    interest = savings.add_interest()
    print(f"Начислено процентов: {interest}")
    print(f"Баланс после начисления: {savings.balance}")

    print("\n=== 7. Полиморфное поведение метода снятия ===")
    accounts = [account, savings]

    for acc in accounts:
        print(f"\n{type(acc).__name__} ({acc.owner}), баланс: {acc.balance}")
        acc.withdraw(100)
        print(f"После снятия 100: {acc.balance}")

    print("\n=== 8. Попытка снять более 50% со сберегательного счёта ===")
    print(f"Баланс {savings.owner}: {savings.balance}")
    big_amount = savings.balance * 0.6
    savings.withdraw(big_amount)

    print("\n=== 9. Проверка, что history возвращает копию ===")
    history_copy = account.history
    history_copy.append("Попытка подменить историю")
    print(f"Реальная история: {account.history}")
    print("Копия не изменила внутренний список — защита работает.")


