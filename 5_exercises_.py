# 5.2


def hello():
    print("Hello, sweetie!")


hello()

# 5.2


def joke():
    print("what does the fox say?")
    print("We may never know.")


joke()

# 5.3


def main():
    joke_line_1()
    joke_line_2()
    joke_line_3()
    joke_line_4()


def joke_line_1():
    print("knock, knock")


def joke_line_2():
    print("whose there?")


def joke_line_3():
    print("interrupting cow.")


def joke_line_4():
    print("interrupting cow wh")
    print("MOO!!!")


main()

# 5.4


def main2():
    name = get_name()
    print("hello ", name)


def get_name():
    name = input("what is your name?")
    return name


main2()

# 5.5


def main3():
    my_number = 7
    square(my_number)


def square(value):
    squared_value = value * value
    print(squared_value)


main3()

# 5.5


def main4():
    num_one = 5
    num_two = 7
    add(num_two, num_one)


def add(two, one):
    total = one + two
    print(total)


main4()

# 5.7

import random  # I don't know why this is showing an error, the error says PEP 8: E402 module level import not at top of file.
pi = 3.14


def main5():
    r = random.randint(1, 10)
    r2 = r * r
    area(r2)


def area(radius_squared):
    my_area = pi * radius_squared
    print(format(my_area, ",.2f"))


main5()

# 5.8


def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds"))
    bmi(height, weight)
    print(bmi(height, weight))


def bmi(height_inches, weight_pounds):
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi = (weight_pounds / (height_inches * height_inches)) * 703
    return format(patient_bmi, '.0f')


main6()

# 5.9

import math  # I don't know why this is showing an error, the error says PEP 8: E402 module level import not at top of file.


def main():
    number_to_round = 4.243
    rounded = math.ceil(number_to_round)
    print('your rounded number is ', rounded)


main()
