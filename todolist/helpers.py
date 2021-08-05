import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import FreqDist
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


testWordList = ['testing', 'hello', 'acceptance testing', 'AT', 'reading', 'watchinng youtube', 'listening to music', 'Testing datetime', 'further testing sigh', 'testingProjects', 'testingProjects2', 'testing again', 'testing once more', 'Singing kumbaya with friends', 'Singing kumbaya with friends', 'Singing kumbaya with friends', 'Singing kumbaya with friends', 'wewe', 'drgfg', 'Watching the olympics', 'testing some stuff']

# function to calculate the frequency of words used across a list
# input is a list of strings
# output is a dictionary of strings and their counts
def findMostCommonWords(listOfLists):

    #global list of words across all the entries
    stringToBeProcessed = []

    # tokenize strings into lists of words and append
    for item in listOfLists:
        tokenizedWords = word_tokenize(item)
        stringToBeProcessed.extend(tokenizedWords)

    # strip stopwords from text
    stoplist = stopwords.words('english')

    processedList = [word for word in stringToBeProcessed if word not in stoplist]
    # find most frequently used n words

    wordFrequencies = FreqDist(processedList)
    mostCommon = wordFrequencies.most_common(10)

    # turn the list of tuples into a dictionary
    mostCommonFinal = {}
    for pairing in mostCommon:
        mostCommonFinal[pairing[0]] = pairing[1]

    return mostCommonFinal

def main():
    #processTime("02:30:00")
    print(findMostCommonWords(testWordList))

main()
