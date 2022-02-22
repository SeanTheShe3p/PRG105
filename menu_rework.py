def main():
    print('hello, welcome to reasons to be vegan.')
    print('please select a meat source to find out more about it')
    print('A: chicken\nB: beef\nC: pork\nD: fish\nE: people')
    selection = input('what would you like to learn not to eat?')
    if selection == 'a' or selection == 'A':
        chicken()
    elif selection == 'b' or selection == 'B':
        beef()
    elif selection == 'c' or selection == 'C':
        pork()
    elif selection == 'd' or selection == 'D':
        fish()
    elif selection == 'e' or selection == 'E':
        people()
    else:
        print('this is not a valid option')
    print('\n*note: your diet is your opinion, this is meant to be humorous')


def chicken():
    print('this is not a food because you dont like chicken nuggets')


def beef():
    print('this is not a food because hamburgers are nasty')


def pork():
    print('this is not a food because bacon is mainly fat')


def fish():
    print('this is not a food because you cant swim')


def people():
    print('this is not a food because that''s cannibalism')


main()
