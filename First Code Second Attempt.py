# # INITIAL CODE

# idx = 0
# file = open('transactions.csv')
# lines = file.readlines()
# for line in lines:
#     print(idx, line)
#     idx = idx + 1
# # dont forget to close file
# file.close()

# # ADDED ENUMERATE AND IF STATEMENT

# idx = 0
# with open('transactions.csv') as file:
#     for idx, line in enumerate(file):
#         if idx == 0:
#             continue
#         print(idx, line)

# # IMPORTING ISLICE

# from itertools import islice
# idx = 0
# with open('transactions.csv') as file:
# # islice function is used within enumerate because islice has to happen first and then enumerate indexes the lines
#     for idx, line in enumerate(islice(file, 1, None)):
# # must call split on the variable identified with the for loop (so line, not file) 
#         fields = line.split(',')
#         print(idx, fields[6], fields[9], fields[11])

# # IGNORE COMMA ALGORITHM

from itertools import islice

def ignoreComma(line): #here my_line gets the alias line for the duration of the function
    fields = []
    chrs = []
    inString = False
    for chr in line:
        # first need to identify if its a field separating comma, or a comma within a field
        if chr == '"':
            # using "not" will flip the boolean
            if inString is not True:
                # '"' will be the start of the string if inString is false, so we need to make it true 
                inString = True
                chrs.append(chr)
            elif inString is True:
                # means we have reached the end of the string within double quotes
                inString = False
                chrs.append(chr)
        elif chr == ',':
            if inString is True:
                chrs.append(chr)
            elif inString is False:
                field = ''.join(chrs) #join turns the list chrs into a string, which we then want to add to the fields list. Dont need the variable name, can also input join into the append method
                fields.append(field) #such as fields.append("".join(field))
                chrs = []
        else:
            chrs.append(chr)
    field = ''.join(chrs)
    fields.append(field)
    return fields # function ignoreComma resolves into a single variable and gets returned to the original location of function in main code

idx = 0
with open('transactions.csv') as file:
    for idx, my_line in enumerate(islice(file, 1, None)):
        my_fields = ignoreComma(my_line) # after function is complete, the returned fields ends up here and is assigned the new name my_fields
        print(idx, my_fields[2], my_fields[4], my_fields[7])