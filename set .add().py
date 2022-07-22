# Showing the use of set{} datatype's .add() function.
# User inputs a number 'N' representing the total number of stamps. 
# Next 'N' lines of input contain the name of countries where the stamp is from. 
# In return, program outputs a number which shows distinct countries stamps.

STDIN = int(input())

countries = set()

for i in range(STDIN):
    country = input()
    countries.add(country)

STDOUT = 0
for i in countries:
    STDOUT += 1
print(STDOUT + "\n")