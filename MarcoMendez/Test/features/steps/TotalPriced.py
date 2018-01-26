

listTotalPriced = {}

def loadTotalPriced():
    listTotalPriced["001"] = 200
    listTotalPriced["002"] = 300
    listTotalPriced["003"] = 400
    listTotalPriced["004"] = 500
    return listTotalPriced

def getPriced(id):
    loadTotalPriced()
    return listTotalPriced.get(id)

print(getPriced("001"))