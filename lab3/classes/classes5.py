class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = 0
    def deposit(self, add_money):
        self.balance += add_money
        print(f"Your balance - {self.balance}")
        return self.balance
    def withdraw(self, taken_money):
        if taken_money <= self.balance:
            self.balance -= taken_money
            print(f"Your balance - {self.balance}")
        else: print("Not enough money on your balance")

bank = Account('Vadim', 0)
bank.deposit(1000)
bank.withdraw(777)
bank.deposit(333)
