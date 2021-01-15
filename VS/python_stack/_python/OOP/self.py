class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposite(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        other_user.make_deposite(amount)
        self.make_withdrawal(amount)

josh = User("Josh", "josh@me.com")
jane = User("Jane", "janedoe@you.com")
mary = User("Mary", "Mary@yoo.com")

josh.make_deposite(100)
josh.make_deposite(300)
josh.make_deposite(200)
josh.make_withdrawal(150)
josh.display_user_balance()

jane.make_deposite(300)
jane.make_deposite(100)
jane.make_withdrawal(50)
jane.make_withdrawal(100)
jane.display_user_balance()

mary.make_deposite(300)
mary.make_withdrawal(150)
mary.make_withdrawal(75)
mary.make_withdrawal(100)
mary.display_user_balance()

josh.transfer_money(mary, 200)
josh.display_user_balance()
mary.display_user_balance()
