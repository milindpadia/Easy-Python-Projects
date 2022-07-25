STDIN = raw_input().split()
x, k = int(STDIN[0]), int(STDIN[1])

P = raw_input()

if eval(P, {'x':x}) == k:
    print(True)
else:
    print(False)
