class Person:
    def __init__(self, name, lastName,age,ci):
        self.Name = name
        self.LastName = lastName
        self.Age=age
        self.CI= ci

    def returInfo(self):
        return self.Name+ ", "+ self.LastName + ", "+  self.Age + ", "+ self.CI