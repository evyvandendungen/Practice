from decimal import Decimal
from csv import DictReader

income = 0
expense = 0

with open('transactions.csv') as file:
    for line in DictReader(file): # DictReader returns a dictionary wherein the key in this case is Amount.
        amount = Decimal(line['Amount'])
        if amount > 0:
            income += amount
        else:
            expense += amount

print("Income:" + str(income))
print("Expenses:" + str(expense))
