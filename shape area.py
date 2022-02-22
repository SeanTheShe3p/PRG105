pi = 3.14


def main():
    menu = 0
    while menu < 5:
        print('please choose the shape for area calculation')
        print('\n1. rectangle\n2. triangle\n3. square\n4. circle\n5. quit\n')
        menu = int(input('what is your shape?'))
        if menu > 4:
            print('goodbye')
        elif menu == 1:
            area = rectangle()
            print('the area of your shape is ', area)
        elif menu == 2:
            area = triangle()
            print('the area of your shape is ', area)
        elif menu == 3:
            area = square()
            print('the area of your shape is ', area)
        elif menu == 4:
            area = circle()
            print('the area of your shape is ', area)
        else:
            print('menu ', menu)


def rectangle():
    base = int(input('what is the base value?'))
    height = int(input('what is the height?'))
    area = base * height
    return area


def triangle():
    base = int(input('what is the base value?'))
    height = int(input('what is the height?'))
    area = .5 * (base * height)
    return area


def circle():
    radius = int(input('what is the radius value?'))
    area = pi * (radius**2)
    return area


def square():
    base = int(input('what is the side value of the square?'))
    area = base**2
    return area


main()
