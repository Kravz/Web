import pickle


class Transaction:

    def __init__(self, amount, date, currency="USD",
                 usd_conversion_rate=1, description=None):
        """
        >>> t = Transaction(100, "2008-12-09")
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (100, 'USD', 1, 100)
        >>> t = Transaction(250, "2009-03-12", "EUR", 1.53)
        >>> t.amount, t.currency, t.usd_conversion_rate, t.usd
        (250, 'EUR', 1.53, 382.5)
        """
        self.__amount = amount
        self.__date = date
        self.__description = description
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate

    @property
    def amount(self):
        return self.__amount

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    @property
    def currency(self):
        return self.__currency

    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate

    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


class Account:
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """

    def __init__(self, number, name):
        """
        Создает новую учетную запись с заданным номером и именем
         Номер используется в качестве имени файла учетной записи.
        """
        self.__number = number
        self.__name = name
        self.__transactions = []

    @property
    def number(self):
        "Номер для чтения"
        return self.__number

    @property
    def name(self):
        """
        Имя учетной записи
        Это может быть изменено, поскольку оно предназначено только для удобства людей;
        номер учетной записи является истинным идентификатором.
        """
        return self.__name

    @name.setter
    def name(self, name):
        assert len(name) > 3, "имя учетной записи не менее 4 символов"
        self.__name = name

    def __len__(self):
        "Возвращает количество транзакций"
        return len(self.__transactions)

    def apply(self, transaction):
        "Применяет (добавляет) данную транзакцию к учетной записи"
        self.__transactions.append(transaction)

    @property
    def balance(self):
        "Возвращает баланс в USD"
        total = 0.0
        for transaction in self.__transactions:
            total += transaction.usd
        return total

    @property
    def all_usd(self):
        "Возвращает True, если все транзакции находятся в USD"
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True

    def save(self):
        "Сохраняет данные учетной записи в файле number.acc"
        fh = None
        try:
            data = [self.number, self.name, self.__transactions]
            fh = open(self.number + ".acc", "wb")
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self):
        """
        Загружает данные учетной записи из файла number.acc
        Все предыдущие данные потеряны.
        """
        fh = None
        try:
            fh = open(self.number + ".acc", "rb")
            data = pickle.load(fh)
            assert self.number == data[0], "номер счета не совпадает"
            self.__name, self.__transactions = data[1:]
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest

    doctest.testmod()