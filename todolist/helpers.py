# function to convert input from a js string into chunks that can be passed to the timedelta python object

def convertJSTime(timeString):
    hours, minutes, seconds = timeString.split(':')
    print(hours, minutes, seconds)

def main():
    convertJSTime("02:30:00")

main()
