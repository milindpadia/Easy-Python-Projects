number_of_test_cases = int(input())

cases = []

for i in range(number_of_test_cases):
    cases.append(input())


for case in cases:
    operands = case.split()
    try:
        division = int(operands[0]) // int(operands[1])
        print(division)
    except ValueError as v:
        print("Error Code:", v)
    except ZeroDivisionError as z:
        print("Error Code:", z)
