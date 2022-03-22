
def main():
    answer = {'zero': 'núll', 'one': 'ein', 'two': 'tvӧ', 'three': 'Þrjú', 'four': 'fjögur', 'five': 'fimm',
              'six': 'sex', 'seven': 'sjö', 'eight': 'átta', 'nine': 'níu', 'ten': 'tíu'}
    grade = 0
    print('þýða úr íslensku yfir á ensku spurningakeppnina:\ntranslate to english quiz\n')
    for num in answer:
        user = input('what is the english for ' + answer[num])
        user = user.lower()
        if num == user:
            print('correct!\n')
            grade += 1
        else:
            print('the answer was not ' + user + ', the answer was ' + num)
    print('you got ', str(grade), ' answers correct\n')
    if grade == 9 or grade == 10:
        print('A')
    elif grade == 8:
        print('B')
    elif grade == 7:
        print('C')
    elif grade == 6:
        print('D')
    else:
        print('you failed!')


main()
