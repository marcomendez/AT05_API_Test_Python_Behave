from Practice5.CalculateAgeInMinutesHoursAndDays import calculateAgeInMinutesHoursAndDays
from Practice5.lengthDictionary import lengthDictionary
from Practice5.lengthDictionary import printDictiory
from Practice5.lengthDictionary import getDirectory
from Practice5.printStatusAge import printStutusAge

#This method load Item in dictonary.
def loadUser():
    lengthDictionary()
    printDictiory()


#print the age in minutes, hours and days
def printAgeToMinutesHourAndDays():
    d = getDirectory()
    for key in d:
        print("-------------------------")
        print( key , "age", d[key])
        calculateAgeInMinutesHoursAndDays(int (d[key] ))
#The expected message according the age define
def printMessageStatusAge():
    d = getDirectory()
    for key in d:
        print("-------------------------")
        print(key, "age", d[key])
        printStutusAge(int(d[key]))




loadUser()
printAgeToMinutesHourAndDays()
printMessageStatusAge()