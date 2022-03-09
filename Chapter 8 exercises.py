# Chapter 8 exercises
#
# 8.2
#
# 1) Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
for character in name:
    print(character)
# 2) Use the index value to access and print the capital s in Schmidt from the variable name
s_value = name[24]
print(s_value)
# 3) Use a negative index value to print the letters from the last name "Schmidt" in name
s_value = name[-7:]
print(s_value)
#
# 8.2
#
# 1) Use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""
# 2) Print middle
middle = name[5:11]
print(middle)
#
# 8.3
#
# 1) Test to see if the string "Jacob" is in name, print the result
if "Jacob" in name:
    print("The name Jacob was found")
else:
    print("no jacob!")
# 2) Test to see if the string "Michael" is in name, print the result
if "Michael" in name:
    print("The name Michael was found")
else:
    print("no michael!")
# 3) Test to see if name contains a number, print the result
    for ch in name:
        if ch.isdigit():
            print("there is a number in name")
# 4) Test to see if number contains a number, print the result
number = "42"
if "42" in number:
    print("42 was found in name")
# 5) Search for "J" in name, replace with "j" (lower case), print the result
#    Note: You can assign this to a variable first, or just print
if "J" in name:
    new_name = name.replace("J", "j")
    print(new_name)
# 6) Split the string name into the variable name_list, replace the "", print the result
name_list = name.split(" ")
print(name_list)
