
class ClientsList:
    listClients = {}
    def __int__(self):
        self.loadClients()

    def loadClients(self):
        self.listClients["001"] = "Marco"
        self.listClients["002"] = "Oscar"
        self.listClients["003"] = "Franco"
        self.listClients["004"] = "Abner"
        self.listClients["005"] = "German"
        self.listClients["006"] = "Karime"

    def getName(self, id):
        self.loadClients()
        name = self.listClients.get(id)
        return str(name)



