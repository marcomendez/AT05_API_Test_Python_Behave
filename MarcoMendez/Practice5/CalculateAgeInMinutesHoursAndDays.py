#Calculate age in minutes, hours and days
def calculateAgeInMinutesHoursAndDays(age):
    """ this method calculate Age in minutes, hours and days """
    diaAux = 365
    minutes = 60
    aDia = 24
    result = diaAux * age
    aHour=60
    print("Age to days", result)
    result = result * aDia
    print("Age to  hours", result)
    result = result * aHour
    print("Age to minutes : ", result)


#calculateAgeInMinutesHoursAndDays(1)