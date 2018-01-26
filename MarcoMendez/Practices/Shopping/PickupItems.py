from Practices.Shopping.Items import Items
from Practices.Shopping.Product import Product

class PickUp:
    listPickUp = {}

    def __init__(self,name):
        self.Client=name

    def addItems(self,items,amount):
        a = Items().getAItem(items)
        a.Amount = amount
        self.listPickUp[items] = a

    def printIemsAdded(self):
        print("==================Items Added==================")
        print("client :" ,self.Client)
        print("items | ","Name           |","amount |","price", "| SubTotal")
        total=0
        for i in self.listPickUp:
            a = self.listPickUp.get(i)
            subtotal =  int(a.Amount) + int(a.Prices)
            total += subtotal
            print(i + "     "+  str(a.Name) + "      " + str(a.Amount) + "        " + str(a.Prices) + "    "+str(subtotal))

        print(" ")
        print("--------------------> Total to Pay = ", total)
        print("=============================================")

    def toBuy(self):
        answer = input("Wish do the buy???  press y / n" )
        if(answer == 'y'):
            for i in self.listPickUp:
                a = self.listPickUp.get(i)
                Items().updateList(i, a.Amount)
            print("=============================================")
            print("Buy successfull")
            print("=============================================")
        else:
            print("=============================================")
            print("Buy cancelled")
            print("=============================================")



list = Items()

list.add("001",Product("productTest 1","100","100"))
list.add("002",Product("productTest 2","200","100"))
list.add("003",Product("productTest 3","300","100"))
list.add("004",Product("productTest 4","400","100"))
list.add("005",Product("productTest 5","500","100"))
list.add("006",Product("productTest 6","60","100"))

list.getAllItems()


pick = PickUp("Maco")
pick.addItems("006",10)
pick.addItems("001",1)
pick.addItems("002",20)
pick.printIemsAdded()
pick.toBuy()



list.getAllItems()
