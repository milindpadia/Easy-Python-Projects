# this program prints following pattern depending upon input size
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

def print_rangoli(size):
    alphabets = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    previous_list = []
    temp_list = []
    reverse_order = []
    no_of_dashes = size * 2 - 2
    for i in range(size, 0, -1):
        temp_list.insert(0, alphabets[i])
        previous_list = temp_list
        the_string = ""
        the_string += alphabets[0] * no_of_dashes
        the_string += "-".join(previous_list[::-1] + temp_list[1:])
        the_string += alphabets[0] * no_of_dashes
        print(the_string)
        reverse_order.append(the_string)
        no_of_dashes -= 2

    reverse_order = reverse_order[::-1]
    for j in range(1, len(reverse_order)):
        print(reverse_order[j])

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
