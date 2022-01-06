user_input = 'random'

def show_menu():
    print('Menu:')
    print('1. Add an item')
    print('2. Mark as done')
    print('3. View items')
    print('4. Exit')

while user_input != '4':

    show_menu()

    user_input = input('>>> ')

    if user_input == '1':
        print('Add an item')
    elif user_input == '2':
        print('Mark as done')
    elif user_input == '3':
        print('View the to do items')
    elif user_input == '4':
        print('Goodbye')
    else:
        print('Please enter one of 1, 2, 3, or 4')