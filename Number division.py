def main():
    user_num = int(input('please enter a number between 20 and 100'))
    valid_number = validate(user_num)
    print('the number: ', valid_number)
    two(valid_number)
    three(valid_number)
    five(valid_number)


def validate(num):
    while 20 >= num or num >= 100:
        num = int(input('please try again.enter a valid number between 20 and 100'))
    return num


def two(number):
    for value in range(2, 101, 2):
        if number == value:
            print('the number is even')


def three(number):
    for value in range(3, 100, 3):
        if value == number:
            print('the number is divisible by 3')


def five(number):
    for value in range(5, 100, 5):
        if number == value:
            print('the number is divisible by 5')


main()
