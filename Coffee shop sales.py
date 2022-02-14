total_sales = 0
daily_sales = 0
for days in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
    daily_sales = float(input("what is the total sales for " + str(days) + "?"))
    total_sales += daily_sales
print("total sales this week: $" + format(total_sales, ',.2f'))
print("average sales per day: $" + format(total_sales/7, ',.2f'))
