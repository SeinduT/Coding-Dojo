class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount (int_rate=0.02, balance=0)
    
    def make_deposite(self, amount):
        self.account.deposite(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        if self.balance < 0:
            print(f"Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            print(f"User: {self.name}, Balance: ${self.account.balance}, Interest rate: {self.account.int_rate}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposite(amount)
        self.make_withdrawal(amount)
        return self

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

josh = User("Josh", "josh@me.com")
jane = User("Jane", "janedoe@you.com")
mary = User("Mary", "Mary@yoo.com")
account1 = BankAccount(5, 100)
account2 = BankAccount(3.5, 75)
account1.deposit(100).deposit(250).deposit(75).withdraw(150).display_account_info()
account2.deposit(200).deposit(100).withdraw(100).withdraw(100).withdraw(150).withdraw(80).display_account_info()