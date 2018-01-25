#replace a word for another
def replace(cad,find,change):
    list = cad.split(find)
    aux = change
    phrase = change.join(list)
    print(phrase)

replace("The rain in Spain...","i","I")
replace("Hello hello yellow","lo","2")