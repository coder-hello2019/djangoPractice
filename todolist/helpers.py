# function to convert input from a js string into chunks that can be passed to the timedelta python object

def processTime(timeString):
    hours, minutes, seconds = timeString.split(':')
    # process each component of HH/MM/SS to remove leading 0s if needed and turn into ints
    if hours[0] == '0':
        hours = int(hours[1])
    else:
        hours = int(hours)

    if minutes[0] == '0':
        minutes = int(minutes[1])
    else:
        minutes = int(minutes)

    if seconds[0] == '0':
        seconds = int(seconds[1])
    else:
        seconds = int(seconds)


    return {'hours': hours, 'minutes': minutes, 'seconds': seconds}

def main():
    processTime("02:30:00")

main()
