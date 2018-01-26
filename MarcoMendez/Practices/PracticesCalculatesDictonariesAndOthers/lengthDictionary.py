# working with dictonaies.

#Variable Global.
dict ={}

#set the length of the dictonary
def lengthDictionary():
    length = int(input(" Dictionary size... "))
    i = 0
    while (i < length):
        key = input(" put key ")
        value = input(" put value ")
        dict[key] = value
        i += 1
    return dict

#Print keys values.
def printKeysDictiory():
    print(dict.keys())

#Print values of the dictonary.
def printValuesDictiory():
    values = dict.values()
    print("Dictonary values", values)

#Print all the dictonary.
def printDictiory():
    print("Dictonary ", dict)

#Print if key exist in the dictonary.
def printKeyExistInDictiory(key):
    print("Key "f"{key}"" = exist" if key in dict else "Key "f"{key}"" =  not exist")

#Print values of the dictonary.
def printValueExistInDictiory(value):
    print("Value "f"{value}"" = exist" if value in dict.values() else "Value "f"{value}"" =  not exist")

#retur all the dictonary.
def getDirectory():
    return dict

#lengthDictionary()
#printKeysDictiory()
#printValuesDictiory()
#printDictiory()
#printKeyExistInDictiory("hola")
#printKeyExistInDictiory("5")
#printValueExistInDictiory("10")
#printValueExistInDictiory("hello")
