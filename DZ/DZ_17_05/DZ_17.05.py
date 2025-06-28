class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value):
        self.new_value = value
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, new_num):
        self.__num = new_num

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, new_perc):
        self.__percent = new_perc

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_balance1(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)

    def print_info1(self):
        print("Информация о счете:")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance1()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def add_percent1(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance1()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято!")

        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()


acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
print()
Account.set_usd_rate(2)
Account.set_eur_rate(2)

acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.add_percent()
print()
acc.surname = "Сорокин"
acc.num = "32456"
acc.percent = 0.04
acc.value = 2000
acc.print_info1()

acc.add_percent1()
print()
acc.withdraw_money(3000)
print()

acc.withdraw_money(1000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)


# Вариант II

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.new_value = value
#         self.__surname = surname
#         self.__num = num
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_balance1(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#     def print_info1(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance1()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def add_percent(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def add_percent1(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance1()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def __set_surname(self, new_surname):
#         self.__surname = new_surname
#
#     def __get_surname(self):
#         return self.__surname
#
#     def __set_num(self, new_num):
#         self.__num = new_num
#
#     def __get_num(self):
#         return self.__num
#
#     def __set_percent(self, new_perc):
#         self.__percent = new_perc
#
#     def __get_percent(self):
#         return self.__percent
#
#     def __set_value(self, new_value):
#         self.__value = new_value
#
#     def __get_value(self):
#         return self.__value
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(2)
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.add_percent()
# print()
#
# acc.surname = "Сорокин"
# acc.num = "32456"
# acc.percent = 0.04
# acc.value = 2000
# acc.print_info1()
#
# acc.add_percent1()
# print()
# acc.withdraw_money(3000)
# print()
#
# acc.withdraw_money(1000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
