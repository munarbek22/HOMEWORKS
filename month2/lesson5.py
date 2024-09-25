# инкапсуляция

# 3 публичный доступ,защищенный,приватный


class BankAccount:
    def __init__(self, name, balance,key):
        self.name = name
        self.__balance = balance
        self._key = key

class Bank:
    def __init__(self, name, balance, key):
        self.name = name
        self.__balance = balance
        self._key = key

    def say(self):
        self._saykey()
    def _saykey(self):
        print(self._key,self.__balance)


b=Bank('John', 100, 2525)
b.name=11
b.key=11111111111
b.Lname='python'
b.say()
b._Bank__balance=323232
b.say()
print(dir(b))