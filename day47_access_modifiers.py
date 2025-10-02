class Employee:
    def __init__(self):
    #  self.name="Rohan"      #public variable
     self.__name="Rohan"      
                            
a=Employee()
# print(a.__name)     #can't access directly
print(a._Employee__name)      #can access indirectly

   
print(a.__dir__())