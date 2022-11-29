user_input = 'random'

to_do_list = []
index = 1

def show_menu():
    print('\n1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit\n')

def remove_item():
    user_input = input("\nEnter the index of item to mark it as done. Enter '0' to cancel operation: ")
    try:
        user_input = int(user_input)
        if user_input == 0:
            return None
        elif type(user_input) == int and user_input <= len(to_do_list):
            to_do_list.pop(user_input - 1)
        else:
            print("Please enter a valid number or enter '0' to cancel operation!")
            remove_item()
    except:
        print("Please enter a valid number or enter '0' to cancel operation!")
        remove_item()

while user_input != '4':

    show_menu()
    user_input = input('Enter your choice: ')

    if user_input == '1':
        task = input('Enter a task to do: ')
        to_do_list.append(task)
    elif user_input == '2':
        print("\nYour tasks:")
        for item in to_do_list:
            print(f"{index}. {item}")
            index += 1
        index = 1
        remove_item()
    elif user_input == '3':
        print("\nYour tasks:")
        for item in to_do_list:
            print(f"{index}. {item}")
            index += 1
        index = 1
    elif user_input == '4':
        print('\nGoodbye\n')
    else:
        print("Please enter '1, 2, 3 or 4' as input!")
