# 4.2
num = 10
while num > 0:
    num = num - 1
    print(num)
# 4.3
for days in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
    print(days)
# 4.3
for numbers in range(10):
    print(numbers + 1)
# 4.4
LOT = 5
total = 0
for addition in range(LOT):
    number = int(input('please enter a number:'))
    total += number
    print('your total is ', total)
# 4.5
number = 0
total = 0
while number != -1:
    calculator = int(input('please input a number into the calculator!'))
    total += calculator
    number = calculator
    print(total)
# 4.6
another = 'y'
while another == 'y':
    number = int(input('enter a number between 1 and 10. '))
    while number > 10 or number < 1:
        print('ERR: Invalid number, try again.')
        number = int(input('enter a new number between 1 and 10.'))
    print('this is a valid number!')
    another = input('would you like to try again?')
