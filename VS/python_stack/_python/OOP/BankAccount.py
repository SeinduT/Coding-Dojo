class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate / 100
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        if self.balance < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            print(f"Interest rate: {self.int_rate}, Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = balance * int_rate
        return self

account1 = BankAccount(5, 100)
account2 = BankAccount(3.5, 75)

account1.deposit(100).deposit(250).deposit(75).withdraw(150).display_account_info()

account2.deposit(200).deposit(100).withdraw(100).withdraw(100).withdraw(150).withdraw(80).display_account_info()