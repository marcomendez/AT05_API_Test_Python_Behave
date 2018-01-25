from Practice5.ClassPractice import Person


class Employee(Person):

    def __init__(self, name, lastName, age,ci,employeeId,department):
        Person.__init__(self,name, lastName,age,ci)
        self.EmployeeId = employeeId
        self.Departmet = department

    def returInfo(self):
        return self.Name+ ", "+ self.LastName + ", "+  self.Age + ", " + self.CI + ", "+ self.EmployeeId + ", "+  self.Departmet



