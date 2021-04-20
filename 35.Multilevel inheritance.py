"""
Multilevel Inheritance:
=======================
one class instance are use another class.
that class was instance was used for another new class.

syntax:
=======

class class1:
    statements

class class2(class1):
    statements

class class3(class2):
     statements


class GrandFather:
    def show1(self):
        print("GrandFather class called...")

class Father(GrandFather):
    def show2(self):
        print("Father class called...")

class Son(Father):
    def show3(self):
        print("son class called...")

g1=GrandFather()
g1.show1()
print()

f1=Father()
f1.show2()
f1.show1()
print()

s1=Son()
s1.show3()
s1.show2()
s1.show1()



class GrandFather:
    cash1=50000
    def show1(self):
        print("GrandFather cash : ",self.cash1)

class Father(GrandFather):
    cash2=30000
    def show2(self):
        print("Father cash : ",self.cash2)
        total=self.cash1+self.cash2
        print("Father access cash :",total)

class Son(Father):
    cash3=1000
    def show3(self):
        print("son cash : ",self.cash3)
        total=self.cash1+self.cash2+self.cash3
        print("Son access cash : ",total)

g1=GrandFather()
g1.show1()
print()

f1=Father()
f1.show2()
f1.show1()
print()

s1=Son()
s1.show3()
s1.show2()
s1.show1()

"""

class GrandFather:
    cash1=50000
    def __init__(self):
        print("GrandFather cash : ",self.cash1)
    def show(self):
        print("GrandFather class....")

class Father(GrandFather):
    cash2=30000
    def __init__(self):
        print("Father cash : ",self.cash2)
        total=self.cash1+self.cash2
        print("Father access cash :",total)
        super().__init__()#call grandfather constructor
        super().show()
        

class Son(Father):
    cash3=1000
    def __init__(self):
        print("son cash : ",self.cash3)
        total=self.cash1+self.cash2+self.cash3
        print("Son access cash : ",total)
        super().__init__()#call father class constructor


g=GrandFather()
print()
f=Father()
print()
s=Son()
