test_cases = int(input())

for case in range(test_cases):
    # first set
    no_of_elements_in_first_set = int(input())
    elements_in_first_set = input()
    first_list = elements_in_first_set.split()
    elements_in_first_set = set(list(map(int, first_list)))

    # second test
    no_of_elements_in_second_set = int(input())
    elements_in_second_set = input()
    second_list = elements_in_second_set.split()
    elements_in_second_set = set(list(map(int, second_list)))

    # check for subset
    print(elements_in_first_set.issubset(elements_in_second_set))

