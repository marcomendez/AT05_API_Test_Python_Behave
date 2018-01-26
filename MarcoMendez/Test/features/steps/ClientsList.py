

listClients = {}

def loadClients():
    listClients["001"] = "Marco"
    listClients["002"] = "Oscar"
    listClients["003"] = "Franco"
    listClients["004"] = "Abner"
    listClients["005"] = "German"
    listClients["006"] = "Karime"

def getName( id):
    loadClients()
    return listClients.get(id)

def addClient(name):
    loadClients()
    listClients[name] = name
