class Budget:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def get_deposit(self):
        amount = int(input("enter the amount to be deposited \n"))
        self.ledger.append({"amount": amount})
        self.balance = self.balance + amount
        return f"This is the amount ${amount} you are depositing into your {self.name} budget"

    def withdraw(self):
        amount = int(input("enter the amount to be withdrawn \n"))
        self.ledger.append({"amount": -amount})
        if self.balance < amount:
            return "Sorry you do not have enough funds in your account"
        else:
            self.balance = self.balance - amount
            return f"your new balance in {self.name} budget is ${self.balance} "

    def get_balance(self):
        return f"Your total balance is ${self.balance} in {self.name}"

    def transfer(self, amount, category):
        if self.balance < amount:
            return "You do not have enough funds in your account "
        else:
            self.balance -= amount
            category.balance += amount
            return f"your transfer of ${amount} from {self.name} to {category.name} was successful"


food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")

print(food.get_deposit())
print(clothing.get_deposit())
print(entertainment.get_deposit())

print(food.withdraw())
print(clothing.withdraw())
print(entertainment.withdraw())

print(food.get_balance())
print(clothing.get_balance())
print(entertainment.get_balance())

print(food.transfer(20, clothing))
print(clothing.transfer(40, food))
print(entertainment.transfer(60, clothing))