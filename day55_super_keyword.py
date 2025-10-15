class Parent:
    def parent_method(self):
        print("I eat mango")
class Child(Parent):
    def Child_method(self):
        print("I eat Apple")
    def parent_method(self):
        print("I eat banana")
        super().parent_method()
child_object=Child()
child_object.Child_method()
child_object.parent_method()

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Boss(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

rohan = Boss("Rohan","2332","English")
print(rohan.lang)