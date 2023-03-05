class Account:

    rate_usd = 0.013
    rate_eur = 0.011
    commission = 0.01
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, number, surname, percent, value=0):
        self.number = number
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.number} принадлежащий {self.surname} был открыт.")
        print("*" * 50)

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print(f"Проценты начислены!")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")
        self.print_balance()

    def add_money(self, val):
        self.value += val - val * Account.commission
        print(f"Комиссия при зачислении {Account.commission:.0%}: {val*Account.commission} {Account.suffix}")
        print(f"{val-val*Account.commission} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"#{self.number}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)

    def __del__(self):
        print("-" * 20)
        print(f"Банковский счет #{self.number} принадлежащий {self.surname} был закрыт")


account1 = Account("12345", "Долгих", 0.03, 1000)
account1.print_info()
account1.convert_to_usd()
account1.convert_to_eur()
print()
account1.set_usd_rate(2)
account1.convert_to_usd()
account1.set_eur_rate(3)
account1.convert_to_eur()
print()
account1.edit_owner("Дюма")
account1.print_info()
print()
account1.add_percent()
print()
account1.withdraw_money(100)
print()
account1.withdraw_money(3000)
print()
account1.add_money(5000)
print()
account1.withdraw_money(3000)

