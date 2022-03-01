def main1():
    in_file = open('sales_totals.txt', 'r')
    count = 0
    total = 0
    for line in in_file:
        amount = float(line.rstrip('\n'))
        print('$' + format(amount, ',.2f'))
        total += amount
        count += 1
    print('$' + format(total, ',.2f') + ' is the total amount')
    print('$' + format(total/count, ',.2f') + ' is the average')
    print('in ' + format(count, ',.0f') + ' line(s)')


main1()
