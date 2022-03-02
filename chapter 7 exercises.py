#
# 7.2
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
new_list = [0] * 5
# 3) Print the contents of your days list using the for operator
for day in days:
    print(day)
# 4) Print the list item that holds the value Saturday from the days list by using its index
print(days[6])
# 5) Create a variable called size to hold the length of the list days using the len function
size = len(days)
# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)
#
# 7.3
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days
work_days = days[1:6]
print(work_days)
#
# 7.4
# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"
if 'Tue' in days:
    print('Tue is in the list')
else:
    print('Tue is not in the list')
#
# 7.5
# 1) Use append() to append the last three months of the year to the list months.
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])
months.append("Oct")
months.append("Nov")
months.append("Dec")
print(months)
# 2) Get the index of "May" from the months list and print it on screen
may_index = months.index("May")
print(may_index)
# 3) Sort list3 from exercise 7.2 and print the results on screen
list3.sort()
print(list3)
# 4) Reverse the order of list3
list3.reverse()
print(list3)
# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)
del list3[-5]
print(list3)
# 6) Print the maximum value from list 3
print(max(list3))
#
# 7.6
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year
months_of_the_year = months
print(months_of_the_year)
#
# 7.7
# 1) Total the values in list3 and print the results
total = 0
for value in list3:
    total += value
print(total)
# 2) Get the average of values in list3 and print the results
total1 = 0
for avg_nums in list3:
    total1 += avg_nums
    average = total1 / len(list3)
print(average)
# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen
states = open('states.txt', 'r')
states_list = states.readlines()
index = 0
while index < len(states_list):
    states_list[index] = states_list[index].rstrip('\n')
    index += 1
print(states_list)
#
# 7.8
# 1) Create a new two-dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31
calendar = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['June', 30], ['July', 31], ['August', 30], ['September', 30], ['October', 31], ['November', 30], ['December', 31]]
# 2) Print the contents of the entire list
print(calendar)
# 3) Print just the values for index 3,0 and 3,1
print(calendar[3][0])
print(calendar[3][1])
#
# 7.9
# Create a tuple using the months list as its data source
months = tuple(months)
print(months)
