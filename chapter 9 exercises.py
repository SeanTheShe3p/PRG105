import pickle
#
# 9.1
#
# 1) Finish creating the following dictionary by adding three more people and birthdays
birthdays = {'Meri': 'May 16', 'Kathy': 'July 14'}
birthdays['Sean'] = 'May 29'
birthdays['Alan'] = 'February 2'
birthdays['Karen'] = 'September 27'
# 2) Print Meri's Birthday
meris_birthday = birthdays['Meri']
print(meris_birthday)
# 3) Create an empty dictionary named registration
registration = {}
# You will use the following dictionary for many of the remaining exercises"
miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}
# 1) Print the keys and the values of miles_ridden using a for loop
for miles in miles_ridden:
    print(miles, miles_ridden[miles])
# 2) Get the value for June 3 and print it, if not found display 'Entry not found', replace the ""
value = miles_ridden.get('June 3', ' entry not found')
print(value)

# 3) Get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
value2 = miles_ridden.get('June 6', 'Entry not found')
print(value2)
# 4) Use the values method to print the miles_ridden dictionary
items = miles_ridden.values()
print(items)
# 5) Use the keys method to print all of the keys in miles_ridden
keys = miles_ridden.keys()
print(keys)
# 6) Use the pop method to remove June 4 then print the contents of the dictionary
popped_day = miles_ridden.pop('June 4')
print(popped_day)
# 7) Use the items method to print the contents of the miles_ridden dictionary
itemized = miles_ridden.items()
print(itemized)
#
# 9.2
#
# 1) Create an empty set named my_set
my_set = set()
# 2) Create a set named days that contains the days of the week
days = set(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
print(days)
# 3) Get the number of elements from the days set and print it
length = len(days)
print(length)
# 4) Remove Saturday and Sunday from the days set
print(days)
days.remove('Saturday')
print(days)
days.remove('Sunday')
print(days)
# 5) Determine if 'Mon' is in the days set
if 'Mon' in days:
    print('Mon was found')
else:
    print('Mon was not found')
#
# 9.3
#
# 1) Import the pickle library at the top of this file
# 2) Create the output file log and open it for binary writing
output_file = open('log.bat', 'wb')
# 3) Pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, output_file)
# 4) Close the log file
output_file.close()
