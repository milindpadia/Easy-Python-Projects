m = int(input())
a = input()
a = set(a.split())
n = int(input())
b = input()
b = set(b.split())

symmetric_difference = a.symmetric_difference(b)
list_ = list(map(int, symmetric_difference))
sorted_list = sorted(list_)

for i in sorted_list:
    print(i)