#Create 1 module to print 4 different messages :
#You are a child, when the age is lower than 12
#Your are teenager, when the age is between 13 and 17
#You are young, when the age is between 18 and 29
#You are adult, when the age is greater than 30
def printStutusAge(age):
    if(age < 12):
        print("You are a child")
    elif(age >= 13 and age <= 17):
        print("Your are teenager")
    elif(age >= 18 and age <= 29):
        print("You are young")
    elif (age >= 30):
        print("You are adult")


#printStutusAge(10)
#printStutusAge(14)
#printStutusAge(20)
#printStutusAge(31)