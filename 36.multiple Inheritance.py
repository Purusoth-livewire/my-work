"""
Multiple Inheritance:
=====================
many parent class
But only one child class

syntax:
=======
class Class1:
    statements

class Class2:
    statements

class Class3(Class1,class2):
    statements


class Father:
    cash1=50000
    def show1(self):
        print("Father cash :",self.cash1)

class Mother:
    cash2=30000
    def show2(self):
        print("Mother Cash :",self.cash2)

class Son(Father,Mother):
    cash3=1000
    def show3(self):
        cash=self.cash1+self.cash2+self.cash3
        print("Son cash :",self.cash3)
        print("Son access cash : ",cash)

f=Father()
f.show1()
print()

m=Mother()
m.show2()
print()

s=Son()
s.show3()
s.show1()
s.show2()


"""
#multiple inheritance using constructor
class Father:
    cash1=50000
    def __init__(self):
        print("Father cash :",self.cash1)

class Mother:
    cash2=30000
    def __init__(self):
        print("Mother Cash :",self.cash2)

class Son(Father,Mother):
    cash3=1000
    def __init__(self):
        cash=self.cash1+self.cash2+self.cash3
        print("Son cash :",self.cash3)
        print("Son access cash : ",cash)
        super().__init__()
        #super().__init__()
s=Son()
