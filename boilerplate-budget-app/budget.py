import math
from itertools import zip_longest


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = self.name.center(30, "*") + "\n"

        for i in range(len(self.ledger)):
            temp = f"{self.ledger[i]['description'][:23] : <23}{'{:.2f}'.format(self.ledger[i]['amount'])[:7] : >7}"
            output += temp + "\n"

        output += f"Total: {self.get_balance()}"

        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is False or len(self.ledger) == 0:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            return True

    def get_balance(self):
        balance = sum(item["amount"] for item in self.ledger)
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount) is True:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    # withdraw, transfer
    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    spent = []
    for category in categories:
        withdraws = 0
        for item in category.ledger:
            if item["amount"] < 0:
                withdraws += abs(item["amount"])
        spent.append(withdraws)

    total = sum(spent)
    percentage = [i / total * 100 for i in spent]

    result = "Percentage spent by category"
    for i in range(100, -1, -10):
        result += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            if j > i:
                result += " o "
            else:
                result += "   "
        result += " "
    result += "\n    ----------"

    cat_length = []
    for category in categories:
        cat_length.append(len(category.name))
    max_length = max(cat_length)

    for i in range(max_length):
        result += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                result += " " + categories[j].name[i] + " "
            else:
                result += "   "
        result += " "

    return result