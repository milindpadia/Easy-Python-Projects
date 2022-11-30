n = int(input())
the_list = input().split()
print(all([all([True if int(i) > 0 else False for i in the_list]), any([True if i == i[::-1] else False for i in the_list])]))
