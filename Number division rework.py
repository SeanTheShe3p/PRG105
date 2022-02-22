def main():
    user_num = int(input('please enter a number between 20 and 100'))
    valid_number = validate(user_num)
    print('the number: ', valid_number)
    two = divisible_by_two(valid_number)
    three = divisible_by_three(valid_number)
    five = divisible_by_five(valid_number)
    output(valid_number, two, three, five)


def validate(num):
    while 20 >= num or num >= 100:
        num = int(input('please try again.enter a valid number between 20 and 100'))
    return num


def divisible_by_two(number):
    if number % 2 == 0:
        return " is divisible by two"
    else:
        return " is not divisible by two"


def divisible_by_three(number):
    if number % 3 == 0:
        return " is divisible by 3"
    else:
        return " is not divisible by 3"


def divisible_by_five(number):
    if number % 5 == 0:
        return " is divisible by 5"
    else:
        return " is not divisible by 5"


def output(num, one, two, five):
    print(str(num) + one)
    print(str(num) + two)
    print(str(num) + five)


main()
