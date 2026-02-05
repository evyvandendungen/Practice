from itertools import islice
# doesnt import the entire module, only what u need. this way you dont have to type the module to attach the method to, ex: itertools.islice(), you can just write the method on its own as a function
def separateField(line):
# naming the function and what it will work on
    in_str = False
    fields = [] # list of str
    chars = []  # list of char

    for chr in line:
        if chr == '"':
            in_str = not in_str

        if chr == ',':
            if not in_str:
                fields.append("".join(chars))
                chars = []
                continue

        chars.append(chr)

    if len(chars):
        fields.append("".join(chars))

    return fields


with open('transactions.csv') as file:
    lines = file.readlines()
    # enumerate should be in the for loop line. still need to include idx in for loop to return a tuple (a pair of variables that cant be changed)
    for idx, line in enumerate(islice(lines, 1, None)):
        # if idx == 0:          <- dont need this if I start enumerating at 1 like shown in line above
        #     continue
        #date = line.split(',')[5]
        #amount = line.split(',')[8]
        #description = line.split(',')[-1]
        fields = separateField(line)
        date = fields[2]
        amount = fields[4]
        description = fields[7]
        # split wants to know which character in the string it should split the string up at, in this case at the comma, and then it wants to know which section to keep, which is set in the square brackets
        print(idx, date, amount, description)
        