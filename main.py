from csv import DictReader

idx = 0
with open('transactions.csv') as file:
    for line in DictReader(file): # if only imported full module, need to include csv. before DictReader
        idx += 1
        print(idx, (f"{line['Posting Date']}, {line['Amount']}, {line['Description']}"))
        # for each variable input, must first reference the variable the file is attached to (line), then within {}, call the list with [], and call the name of the list you want to print from.