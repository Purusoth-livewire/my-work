"""
Inheritance:
============
To access the one class information into another class

#parent class/base class/super class
#child class/sub class/derived class

syntax:
=======
class class1:#parent class
    statements
class class2(class1):#child class
    statements
"""

#program

class Class1:#parent class---it can access itself data and provide itself data to child clkass
    #but it cant access child class data to here.
    name1="janani"
    def show1(self):
        print("name : ",self.name1)

class Class2(Class1):#child class---access their parent property
    name2="jeeva"
    def show2(self):
        print("name : ",self.name1)
        print("name : ",self.name2)


c1=Class1()
c1.show1()
#c1.show2()#class1 cant access class 2 information

c2=Class2()
c2.show1()#class 2 can access the information for itself and herited class also
c2.show2()

"""
