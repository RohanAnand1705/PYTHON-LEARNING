class Employee:
    def __init__(self, name , id):
        self.name= name
        self.id= id
    def showDetails(self):
        print(f"The name of employee: {self.id} is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("Python")

e =Employee("Rohan", 1000)
e.showDetails()
e2 =Programmer("Mohan", 2000)
e2.showDetails()
e2.showLanguage()

