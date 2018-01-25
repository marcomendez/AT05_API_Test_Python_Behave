from Practice5.Shopping.Product import Product


class Items(Product):
    ListItems = {}

    def __init__(self):
        self.Items=""

    def add(self,key,value):
        self.ListItems[key] = value

    def getAllItems(self):
        print("==================Inventary==================")
        print("Name            |  Price    |  Amount   ")
        for i in self.ListItems:
            a = self.ListItems.get(i)
            prod= Product(a.Name,a.Prices,a.Amount)
            print(prod.Name,"      "+ str(prod.Prices) ,"        "+ str(prod.Amount))
        print("=============================================")

    def getAItem(self, item):
        a = self.ListItems.get(item)
        prod = Product(a.Name, a.Prices, a.Amount)
        return  prod

    def updateList(self, items, value):
        a = self.getAItem(items)
        a.Amount = int(a.Amount) - int(value)
        self.ListItems[items] = a

