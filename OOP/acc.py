class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""

    # this is a class variable
    type = "checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


jacks_checking = Checking("jack.txt", 1)
jacks_checking.transfer(10)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)


# doc string, very important for knowing the class information
print(jacks_checking.__doc__)

johns_checking = Checking("john.txt", 1)
johns_checking.transfer(10)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

account = Account("balance.txt")

print(account.balance)

account.withdraw(100)

print(account.balance)

account.commit()

print(account.balance)

