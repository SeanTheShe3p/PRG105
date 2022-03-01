def main():
    number = int(input('How many people are you adding?'))
    address = open('addresses.txt', 'w')
    for person in range(0, number):
        name = input('what is the name of person ')
        phone_num = input('what is the phone number of person')
        email_add = input('what is their email address?')
        address.write(name + ' , ' + email_add + ' , ' + phone_num + '\n')
    address.close()


main()
