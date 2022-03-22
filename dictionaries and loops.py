
def main():
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    daily_values = {}
    mini_steps = 20000000
    maxi_steps = 0
    total_steps = 0
    maxi_days = []
    mini_days = []
    print('you will be entering your steps for the week')
    for day in days:
        steps = int(input('how many steps did you take on ' + day + '?'))
        daily_values[day] = steps
        total_steps += steps
    mini_steps = min(daily_values.values())
    maxi_steps = max(daily_values.values())
    for key, value in daily_values.items():
        if maxi_steps == value:
            maxi_days.append(key)
        if mini_steps == value:
            mini_days.append(key)
    average = total_steps / len(daily_values)
    print('the total steps you took was ', str(total_steps))
    print('the average steps you took was ', format(average, '.2f'))
    print('the most steps you took was ', str(maxi_steps), ' on ')
    for day in maxi_days:
        print(str(day))
    print('the least steps you took was ', str(mini_steps), ' on ')
    for day in mini_days:
        print(str(day))


main()
