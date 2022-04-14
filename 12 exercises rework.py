# 12.1
# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested


def main():
    hooray(5)


def hooray(number):
    if number > 0:
        print('Hooray!')
        number = number - 1
        hooray(number)
    else:
        print()
# 2) Call the function with a parameter value of 5.


main()

# 12.2-12.3
# 1) Create a function that uses recursion to sum the numbers in a list.
#    The function should have one parameter, the list of numbers,
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.

# 2) Call the function using the numbers list as a parameter


def main1():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(numbers)
    math(numbers)


def math(num):
    if len(num) > 1:
        num[len(num) - 1] = num[len(num) - 1] + num[len(num) - 2]
        num.pop(len(num) - 2)
        print(num)
        math(num)
    else:
        print(num[0])


main1()
