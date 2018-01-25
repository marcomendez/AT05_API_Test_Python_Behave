#Function that will create a dictionary with a list of userID and userName,
# the userID should be only numbers between 1 to 100. Username should be
# only lowercase (nor more than 8 digits)
import re
#Variable global
dict = {}
#Dictonary that allow number between 1 - 100
def DictionaryAllowNumber1To100(key,value):
    cad=""
    cad=value
    if(key > 0  and key <= 100 and len(value) <= 8 and cad.islower()):
        dict[key]=value

# method that search by IdUser.
def searchNumberId(idUser):
    result = [ ]
    reObj = re.compile(str(idUser))
    for key in dict.keys():
        if (reObj.match(str(key))):
            result.append(key)
    return result

#search characters start value
def searchCharacterStartValue(valueStart):
    result = []
    for valuesName in dict.values():
        if (str(valuesName).startswith(valueStart)):
            result.append(valuesName)
    return result

#Function to display a message considering :
#UseID between 1-25 “User belong Group 1”
#UseID between 26-50 “User belong Group 2”
#UseID between 51-75 “User belong Group 3”
#UseID between 76-100 “User belong Group 4”
def displayMessageForGroup():

    for userId in dict.keys():
        if(userId >=1 and userId <= 25 ):
            print("UserId",userId," belong Group 1")
        elif (userId >=26 and userId <= 50 ):
            print("UserId",userId," belong Group 2")
        elif (userId >=51 and userId <= 75):
            print(userId," belong Group 3")
        elif ("UserId",userId >=76 and userId <= 100):
            print("UserId",userId," belong Group 4")

#Function to print the array received
def printArray(array):
    print("Array printed: " ,array)

DictionaryAllowNumber1To100(1,"marco")
DictionaryAllowNumber1To100(2,"oscar")
DictionaryAllowNumber1To100(3,"maria")
DictionaryAllowNumber1To100(4,"pedro")
DictionaryAllowNumber1To100(5,"marta")
DictionaryAllowNumber1To100(6,"carmen")
DictionaryAllowNumber1To100(7,"cesar")
DictionaryAllowNumber1To100(8,"franco")
DictionaryAllowNumber1To100(9,"jorge")
DictionaryAllowNumber1To100(10,"favio")
DictionaryAllowNumber1To100(11,"andrea")
DictionaryAllowNumber1To100(12,"marioly")
DictionaryAllowNumber1To100(100,"keila")

print(searchNumberId(1))
print(searchNumberId(2))
print(searchCharacterStartValue("m"))

displayMessageForGroup()

printArray(searchNumberId(1))
printArray("m")