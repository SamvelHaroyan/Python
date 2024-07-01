class BankUser:
    @staticmethod
    def _is_valid_account_number(a):
        return (isinstance(a, str)
                and (len(a) == 16 and a.isdigit() or
                     len(a) == 19 and (a[:4] + a[5:9] + a[10:14] + a[15:]).isdigit() and a[4::5] == '   '))

    @staticmethod
    def _money_account(account_money):
        return isinstance(account_money, int | float) and account_money > 0

    @staticmethod
    def _is_valid_name_surname(user_name, user_surname, age):
        return (isinstance(user_name, str) and isinstance(user_surname, str) and isinstance(age, int) and
                user_name.isalpha() and user_surname.isalpha() and age > 0)

    @staticmethod
    def _is_valid_parol(password):
        return isinstance(password, str) and len(password) > 8

    def __init__(self, name, surname, age, account_number, account_money, password):
        if (self._is_valid_account_number(account_number) and self._is_valid_name_surname(name, surname, age)
                and self._money_account(account_money) and self._is_valid_parol(password)):
            self._name = name
            self._surname = surname
            self._age = age
            self.__account_number = account_number
            self.__account_money = account_money
            self.__password = password
            self.__count_enter_parol = 3
            self.__blocked = False
        else:
            raise ValueError('Error Invalid..Bye!')

    def info_person(self):
        if self._bloc():
            print(f'Անուն՝ {self._name} Ազգանուն ՝ {self._surname} Տարիք ՝{self._age}')

    def _passw(self):
        if input('Enter your password: ') == self.__password:
            return True
        self.__count_enter_parol -= 1
        print('Invalid password.')
        if self.__count_enter_parol == 0:
            self.__blocked = True
            print('Your account is blocked.')
        return False

    def _bloc(self):
        if self.__blocked:
            print('Your account was blocked.')
            return False
        return True

    def info_card(self):
        if self._bloc():
            if self._passw():
                print(f"Բանկային քարտի համար ՝ {self.__account_number}, Հաշվի մնացորդ ՝ {self.__account_money} դրամ")

    def add_money(self, mon):
        if self._bloc():
            if self._passw():
                if self._money_account(mon):
                    self.__account_money += mon
                else:
                    print('Invalid argument.')

    def sub_money(self, mon):
        if self._bloc():
            if self._passw():
                if self._money_account(mon):
                    if mon <= self.__account_money:
                        self.__account_money -= mon
                    else:
                        print('Not enough money.')
                else:
                    print('Invalid argument.')

    def unblock(self):
        p = input('Enter your password: ')
        card = input('Enter last 4 numbers of your card: ')
        age = input('Enter your age: ')
        if p == self.__password and card == self.__account_number[-4:] and str(self._age) == age:
            self.__count_enter_parol = 3
            self.__blocked = False
            print('Your card is unblocked.')
        else:
            print('Invalid information.')


# user1 = BankUser('Վազգեն', 'Ասրյան', 21, '4444 5555 6666 8888', 5000, 'qwerty123')
# user1.info_person()
# user1.info_card()
# user1.info_card()
# user1.info_card()
# user1.info_card()
# user1.info_person()

