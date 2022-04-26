import pickle
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open('customer_data.bat', 'rb')
        customers = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        print('file not found')
        customers = {}
    choice = 0
    while choice != QUIT:
        print(customers)
        choice = menu()
        if choice == LOOKUP:
            lookup(customers)
        if choice == ADD:
            add(customers)
        if choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            choice = QUIT
            print('Goodbye!')


def menu():
    print('Menu\n______________\nLOOKUP = 1\nADD = 2\nCHANGE = 3\nDELETE = 4\nQUIT = 5')
    choice = int(input('please select'))
    while 1 > choice > 5:
        choice = 5
    return choice


def lookup(customers):
    name = input('what is the customers name?')
    if name in customers:
        print(name, ' : ', customers[name])
    else:
        print(name, ' was not found')


def add(customers):
    user_name = input('what is the name to add?')
    user_email = input('what is the user email')
    customers[user_name] = user_email
    print('Thank you, customer ' + user_name + ' has been added')
    save_file(customers)


def change(customers):
    name = input('what is the customers name?')
    if name in customers:
        email = input('what is the new email')
        customers[name] = email
        save_file(customers)
    else:
        print(name, ' was not found')


def delete(customers):
    name = input('who to delete?')
    print(name, ' : ', customers[name])
    confirm = input('are you sure? y/n')
    if confirm.lower() == 'y':
        del customers[name]
        save_file(customers)
    else:
        save_file(customers)


def save_file(customers):
    output_file = open('customer_data.bat', 'wb')
    pickle.dump(customers, output_file)


main()
