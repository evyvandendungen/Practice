from decimal import Decimal
import csv

def calculate_totals(reader): #separate what you want code to do from where you open the file
    income = Decimal(0) #initialized into a string
    expense = Decimal(0)

    for fields in reader:
        amount = Decimal(fields["Amount"])
        if amount > 0:
            income += amount
        else:
            expense += abs(amount)

    return income, expense
with open("transactions.csv") as file:
    reader = csv.DictReader(file) #dont forget to capitalize the R as well
    total_income, total_expenses = calculate_totals(reader)
    print(f"total income: {total_income}, total expenses: {total_expenses}") #{} contains expressions

# with open('transactions.csv') as file:
#     for line in DictReader(file): # DictReader returns a dictionary wherein the key in this case is Amount.
#         amount = Decimal(line['Amount'])
#         if amount > 0:
#             income += amount
#         else:
#             expense += abs(amount) #abs is absolute value of a number

# print("Income:" + str(income))
# print("Expenses:" + str(expense))
