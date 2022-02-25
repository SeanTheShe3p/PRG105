# 6.1


def main():
    states = open('states.txt', 'r')
    states.close()
    state_capitals = open('capitals.txt', 'w')
    state_capitals.write('Montgomery, Alabama\n')
    state_capitals.write('Juneau, Alaska\n')
    state_capitals.write('Phoenix, Arizona\n')
    state_capitals.close()


main()

# 6.1


def main1():
    states_data = open('states.txt', 'r')
    line1 = states_data.readline()
    line2 = states_data.readline()
    line3 = states_data.readline()
    states_data.close()
    print(line1, line2, line3)


main1()

# 6.2


def main2():
    states_file = open('states.txt', 'r')
    counter = 0
    for lines in states_file:
        counter += 1
        print(counter)
        print(states_file.readline())
    states_file.close()


main2()

# 6.3


def main3():
    books = 3
    books_file = open('books.txt', 'w')
    for strings in range(1, books + 1):
        title = input('what is the title?')
        author = input('what is the authors name?')
        books_file.write(title + ' - ' + author + '\n')
    books_file.close()


main3()

# 6.4


def main3():
    try:
        superheroes = open('superheroes.txt', 'r')
        superheroes.close()
        print('file is opened and closed')
    except IOError:
        print('the file does not exist')


main3()
