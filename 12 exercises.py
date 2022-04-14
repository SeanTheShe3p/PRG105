# 12.1
# 1) Using program 12-2 as an example, create a recursive function.
#    The function should print "Hooray!" the number of times requested
#    by the parameter times_requested
def main(number):
    if number > 0:
        print('Hooray!')
        number = number - 1
        main(number)
    else:
        print()
# 2) Call the function with a parameter value of 5.


main(5)
# 12.2-12.3
# 1) Create a function that uses recursion to sum the numbers in a list.
#    The function should have one parameter, the list of numbers,
#    and it should return the sum of the list values.
# Hint: Each iteration should remove one item from the list.
# The recursion should end when all items have been removed from the list.

# 2) Call the function using the numbers list as a parameter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def main(timer):
    count = 0
    if timer > 0:
        for num in numbers:
            count += num
        del numbers[len(numbers) - 1]
        timer = timer - 1
        print(count)
        main(timer)
    else:
        print("that's it!")


main(len(numbers))
