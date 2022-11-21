# this program prints the following pattern for input: 7 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# input should be two numbers which are single space seperated
# where first number is number of rows and second number is columns i.e. 3 times the first number

user_input = input("Size: ")
rows = int(user_input.split()[0])
columns = int(user_input.split()[1])
dash = "-"
pattern = ".|."
no_of_patterns = 1
no_of_dashes = (columns - 3) // 2

for i in range(0, rows):
    if i == (rows // 2):
        print(dash * ((columns - 7) // 2) + "WELCOME" + dash * ((columns - 7) // 2), end="")
    elif i < rows // 2:
        print(dash * no_of_dashes, end="")
        print(pattern * no_of_patterns, end="")
        print(dash * no_of_dashes, end="")
        no_of_patterns += 2
        no_of_dashes -= 3
    else:
        no_of_patterns -= 2
        no_of_dashes += 3
        print(dash * no_of_dashes, end="")
        print(pattern * no_of_patterns, end="")
        print(dash * no_of_dashes, end="")
    print()
