class Employee:
    company_Name="Apple"
    noOfEmployees = 0
    def __init__(self,name):
       self.name = name
       self.raise_amount = 0.02
       Employee.noOfEmployees+=1
    def showDetails(self):
        print(f"Name of employee is {self.name} and the raise amount is {self.noOfEmployees} sized company {self.company_Name} is {self.raise_amount}")

emp1=Employee("Rohan")
emp1.raise_amount= 0.3
emp1.company_Name= "Apple_India"
emp1.showDetails()
emp2=Employee("Mohan")
Employee.company_Name="Google"
emp2.showDetails()

# Employee.showDetails(emp1)