def main():
    sales = open('sales_totals.txt', 'r')
    count = 0
    total = 0
    sales_value = sales.readline()
    while sales_value != '':
        sales_value = sales_value.rstrip('\n')
        total += float(sales_value)
        sales_value = float(sales_value)
        print('$' + format(sales_value, ',.2f'))
        count += 1
        sales_value = sales.readline()
    print('your total sales are $', format(total, ',.2f'))
    print('your average sales are $', format(total / count, ',.2f'))
    print('in ', count, ' lines')


main()
