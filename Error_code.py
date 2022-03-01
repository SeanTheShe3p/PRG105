def main1():
    try:
        err_file = open('sales_error.txt', 'r')
    except IOError:
        print('the file is invalid')
    count = 0
    total = 0
    for line in err_file:
        try:
            amount = float(line.rstrip('\n'))
            print('$' + format(amount, ',.2f'))
            total += amount
            count += 1
        except ValueError:
            print('the value is invalid')
    print('$' + format(total, ',.2f') + ' is the total amount')
    print('$' + format(total/count, ',.2f') + ' is the average')
    print('in ' + format(count, ',.0f') + ' line(s)')


main1()
