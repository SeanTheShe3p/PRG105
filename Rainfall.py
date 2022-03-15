
def main():
    rainfall = open('rainfall-totals.txt', 'r')
    total = 0
    error = []
    for line in rainfall:
        line = line.rstrip('\n')
        line = line.split()
        month = line[0]
        rain = line[1]
        rain = rain.split('.')
        try:
            rain = rain[0] + rain[1]
            rain = format(float(rain)/10, '.1f')
            total += float(rain)
        except ValueError:
            error.append('the value ' + month + ' was invalid')
            rain = ''
        line[1] = rain
        print(str(line[0] + ' ' + line[1]))
    print('the total valid rainfall was ' + format(total, '.1f'))
    print('the average was ' + format(total / 11, '.1f') + ' rainfall')
    print(error)


main()
