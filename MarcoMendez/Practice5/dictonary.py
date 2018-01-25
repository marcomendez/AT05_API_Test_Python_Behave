import operator
#short a dict
def dict(cad):
    i = 0
    cont = 0;
    dictResul = {}
    while i <= len(cad)-1 :
        j = 0
        cont = 0
        while j <= len(cad)-1:
            if cad[j].lower() == cad[i].lower():
                cont += 1
            j += 1
        if cont >0 and cad[i]!=" ":
            dictResul[cad[i].lower()] = cont
        i += 1
    print(sorted(dictResul.items(), key=operator.itemgetter(0)))

dict("ThiS is string with upper and Lower case letters")
dict("hello yellow caramelo")