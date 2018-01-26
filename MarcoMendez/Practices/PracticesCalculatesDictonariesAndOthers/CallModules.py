from Practices.CalculateAgeInMinutesHoursAndDays import calculateAgeInMinutesHoursAndDays
from Practices.printStatusAge import printStutusAge

from Practices.PracticesCalculatesDictonariesAndOthers.lengthDictionary import getDirectory
from Practices.PracticesCalculatesDictonariesAndOthers.lengthDictionary import lengthDictionary
from Practices.PracticesCalculatesDictonariesAndOthers.lengthDictionary import printDictiory


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