# def print_rangoli(size):
#     # your code goes here

# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)

size = 5
alphabets = ['-', 'a', 'b', 'c', 'd', 'e']
dash = "-"

for i in range(1, size*2):
    print(dash * ((size * 2) -2) + alphabets[size] + dash * ((size * 2) -2))
    size -= 1
