my_string = input('please enter a string to acronym')
my_list = my_string.split(' ')
acronym = []
for words in my_list:
    first_letter = words[0]
    acronym.append(first_letter)
print(acronym)
