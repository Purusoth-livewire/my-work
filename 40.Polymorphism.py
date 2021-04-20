"""
Polymorphism:
=============
Poly===many
morphism---form
poly+morphism---->many form

To ability to do a different task.

overloading:
    function overloading
    operator overloading
Function  overriding


function overloading:
=====================

def area(a,b):
    c=a+b
    print(c)


area(10,20)
area("wel","come")


Function Overriding:
====================


class Class1:
    def show(self):
        print("parent class called...")

class Class2(Class1):
    def show(self):
        print("child class called...")
        super().show()

c=Class2()
c.show()#only call child class
#c.show()

Operator Overloading:
=====================

"""

class KsMess:
    def __init__(self,collection):
        self.collection=collection

    def __add__(self,other):
        print("Karur Collection : ",self.collection)
        print("Trichy Collection : ",other.collection)
        total=self.collection+other.collection
        print("Total Collection : ",total)


karur=KsMess(45000)
trichy=KsMess(44000)
karur+trichy
