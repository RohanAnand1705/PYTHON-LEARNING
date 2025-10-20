#Hybrid Inheritance
class Baseclass:
    pass

class Derived1(Baseclass):
    pass
class Derived2(Baseclass):
    pass
class Derived3(Derived1, Derived2):
    pass

#Hierarchical Inheritance

class Baseclass1:
    pass
class D1(Baseclass1):
    pass
class D2(D1):
    pass