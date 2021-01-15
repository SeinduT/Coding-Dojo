class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposite(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposite(amount)
        self.make_withdrawal(amount)
        return self

josh = User("Josh", "josh@me.com")
jane = User("Jane", "janedoe@you.com")
mary = User("Mary", "Mary@yoo.com")

josh.make_deposite(100).make_deposite(300).make_deposite(200).make_withdrawal(150).display_user_balance()

jane.make_deposite(300).make_deposite(100).make_withdrawal(50).make_withdrawal(100).display_user_balance()

mary.make_deposite(300).make_withdrawal(150).make_withdrawal(75).make_withdrawal(100).display_user_balance()

josh.transfer_money(mary, 200).display_user_balance()
mary.display_user_balance()
