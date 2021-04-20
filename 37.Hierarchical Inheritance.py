"""
Hierarchical Inheritance:
=========================
Only one parent class but
multiple child class

syntax:
=======
class Class1:
    statements
class Class2(Class1):
    statements
class Class3(Class1):
    statements
"""

class Father:
    cash1=50000
    def show1(self):
        print("Father cash : ",self.cash1)

class Son1(Father):
    cash2=5000
    def show2(self):
        cash=self.cash1+self.cash2
        print("Son1 cash :",self.cash2)
        print("son1 access cash :",cash)

class Son2(Father):
    cash3=1000
    def show3(self):
        cash=self.cash1+self.cash3
        print("son2 cash :",self.cash3)
        print("son2 access cash :",cash)       

f=Father()
f.show1()
print()
s1=Son1()
s1.show2()
s1.show1()
print()
s2=Son2()
s2.show3()
s2.show1()

