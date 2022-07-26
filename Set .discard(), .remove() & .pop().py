n = int(input())
s = set(map(int, input().split()))
no_of_commands = int(input())

# operations on set
for i in range(no_of_commands):
    command = input().split()
    if command[0] == 'remove':
        try:
            s.remove(int(command[1]))
        except KeyError:
            continue
    elif command[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            continue
    else:
        s.discard(int(command[1]))

# sum of elements in set
sum = 0
for i in s:
    sum += i

print(sum)
