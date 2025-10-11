class Employee:
    company="Apple"
    def show(self):
        print(f"The name of employee is {self.name} and name of company is {self.company}")
    @classmethod
    def changecompany(cls, newcompany):
        cls.company=newcompany
e1=Employee()
e1.name= "Rohan"
e1.show()
e1.changecompany("Tesla")
e1.show()
print(Employee.company)