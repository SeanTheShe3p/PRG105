
def main():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    daily_values = {}
    mini_steps = 20000000
    maxi_steps = 0
    total_steps = 0
    print('you will be entering your steps for the week')
    for day in days:
        steps = int(input('how many steps did you take on ' + day + '?'))
        daily_values[day] = steps
        total_steps += steps
    mini_steps = min(daily_values.values())
    maxi_steps = max(daily_values.values())
    average = total_steps / len(daily_values)
    print('the total steps you took was ', str(total_steps))
    print('the average steps you took was ', format(average, '.2f'))
    print('the most steps you took was ', str(maxi_steps), ' on ')
    for key in daily_values:
        if daily_values[key] == maxi_steps:
            print('\t', str(key))
    print('the least steps you took was ', str(mini_steps), ' on ')
    for key in daily_values:
        if daily_values[key] == mini_steps:
            print('\t', str(key))


main()
