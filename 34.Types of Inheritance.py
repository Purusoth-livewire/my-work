"""
Types of Inheritance:
=====================
1.single inheriatnce
2.multilevel Inheritane
3.multiple Inheritane
4.Hierarchical Inheritane
5.Hybrid Inheritane


1.single inheriatnce:
=====================
only one parent class
only one child class

syntax:
=======
class Class1:
     statements
class class2(class1):
    statements
    
#program
class Father:
    cash1=50000
    def show1(self):
        print("Father cash : ",self.cash1)

class Son(Father):
    cash2=20000
    def show2(self):
        total=self.cash1+self.cash2
        print("son cash : ",self.cash2)
        print("son access cash : ",total)
f=Father()
f.show1()

s=Son()
s.show2()
s.show1()

"""
#program
class Father:
    cash1=50000
    def __init__(self):
        print("Father cash : ",self.cash1)

class Son(Father):
    cash2=20000
    def __init__(self):
        total=self.cash1+self.cash2
        print("son cash : ",self.cash2)
        print("son access cash : ",total)
        super().__init__()#call super class constructor
f=Father()
print()
s=Son()

