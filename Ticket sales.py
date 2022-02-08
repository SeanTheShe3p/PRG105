print('Hello! And welcome to the play! We have discounts for senior, veterans, students and of course show sponsors.')
print('Tickets also are discounted at 10% between 4 and 8 tickets, 15% for 9-15 tickets and more than 15')
print('gets a 20% discount! Enjoy the show')
print('Tickets!\n1.) General Admission $10\n2.) Veterans $7\n3.) Seniors $6\n4.) Students $5\n5.) Sponsors $2\n')
ga = int(10)
va = int(7)
sen = int(6)
std = int(5)
sos = int(2)
ticket = input('Please enter the number of your choice.')
if ticket == '1':
    ticket_price = ga
elif ticket == '2':
    ticket_price = va
elif ticket == '3':
    ticket_price = sen
elif ticket == '4':
    ticket_price = std
elif ticket == '5':
    ticket_price = sos
else:
    ticket_price = 10
ticket_number = int(input('How many tickets would you like?'))
if ticket_number > 15:
    discount = float(.8)
elif ticket_number >= 8:
    discount = float(.85)
elif ticket_number <= 4:
    discount = float(.9)
else:
    discount = 0
print('Your price before discounts is $' + format(ticket_price * ticket_number, ',.2f') + '.')
print('The price after discount is $' + format((ticket_price * ticket_number) * discount, ',.2f') + '.')
print('A ticket price of $' + format(ticket_price * discount, ',.2f'))
