m = int(input())
a = input()
a = set(a.split())
n = int(input())
b = input()
b = set(b.split())

# symmetric difference
symmetric_difference = a.symmetric_difference(b)

# converting strings to integers using 'map' function and converting set to list
list_ = list(map(int, symmetric_difference))

# sorting and printing the items in list
sorted_list = sorted(list_)
for i in sorted_list:
    print(i)
