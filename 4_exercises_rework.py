
# 4.2
num = 10
while num > 0:
    num = num - 1
    print(num)

# 4.3
for days in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
    print(days)

# 4.3
for numbers in range(1, 11):
    print(numbers)

# 4.4 rework
total = 0
for numbers in range(1, 6):
    number = int(input("please enter a number"))
    total += number
    print("the total of the numbers is " + str(total))

# 4.4
LOT = 5
total = 0
for addition in range(LOT):
    number = int(input('please enter a number:'))
    total += number
    print('your total is ', total)

# 4.5 rework
total = 0
count = 0
score = 0
while score >= 0:
    score = int(input("please enter a test score, put -1 when finished."))
    total += score
    count += 1
print("you entered " + str(count) + " score(s)")
print("the total score was " + format(total, ',.0f'))
print("the average score was " + format(total/count, ',.1f'))

# 4.5
number = 0
total = 0
while number != -1:
    calculator = int(input('please input a number into the calculator!'))
    total += calculator
    number = calculator
    print(total)

# 4.6 rework
num = 0
while num < 1 or num > 10:
    num = int(input("please enter a number between 1 and 10."))

# 4.6
another = 'y'
while another == 'y':
    number = int(input('enter a number between 1 and 10. '))
    while number > 10 or number < 1:
        print('ERR: Invalid number, try again.')
        number = int(input('enter a new number between 1 and 10.'))
    print('this is a valid number!')
    another = input('would you like to try again?')
