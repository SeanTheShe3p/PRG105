# 3.1 - variables
a = 6
b = 8
c = 5
if c < 10:
    print('c < 10')
if a == c:
    print('a == c')
if a != c:
    print('a != c')
if a <= c:
    print('a <= c')

# 3.2
age = int(input('what is your age? '))
if age >= 18:
    print('you are old enough to vote!')
else:
    print('you are not old enough to vote...')

# 3.2
password = "narwhals"
user_password = input("Please enter the password:  ")
if user_password == password:
    print('this is correct')
else:
    print('that is not correct')

# 3.4
number = int(input("Please enter a number between 1 and 5: "))
if number == 5:
    print('V')
elif number == 4:
    print("IV")
elif number == 3:
    print('III')
elif number == 2:
    print('II')
elif number == 1:
    print('I')
else:
    print('this is not a valid number.')

# 3.5
customer_age = int(input("How old is the customer?   "))
cost = 0
if customer_age >= 62:
    cost = 9.89
if customer_age <= 61:
    if customer_age >= 12:
        cost = 12.89
if customer_age <= 11:
    if customer_age >= 3:
        cost = customer_age * 0.99
else:
    cost = 0

print("Your cost for a customer who is " + str(customer_age) + " years old")
print("is $" + format(cost, ",.2f"))
# 3.5
d = 10
e = 10
f = 12
if d == e and d < f:
    print('d == e and d < f')
if d < f or e > d:
    print('d < f or e > d')
if not d == f:
    print('d != f')

# 3.6
tired = True
hungry = False
if tired:
    print('eyes open')
else:
    print('eyes closed')
if hungry:
    print('crying')
else:
    print('quiet')
