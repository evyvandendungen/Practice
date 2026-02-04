idx = 0
with open('transactions.csv') as file:
    lines = file.readlines()
    for line in lines:
        print(idx, line)
        idx = idx + 1
