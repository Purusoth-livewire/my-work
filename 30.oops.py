"""
Oops:
====
Object oriented programs
program are writes based on  object.

A object contain a set of attributes and behaviour.

example 1:

object:human
attributes---name,age,gender,colour,DOB,mobile,address
behaviour----walking,running,jumping,speaking,sleeping,laughing,eating

example 2:
object : bird
attributes----name,age,gender,colour
behaviour-----flying,eating,singing

example 3 :

object : vegetable

atttributes: name,colour
behaviour : taste

oops :
=======
1.object
2.class
3.inheritance
4.polymorphism
5.data abstraction
6.data Encapsulation


class:
======
it is a prototype(blueprint) of object.

Syntax:
=======
(identifier----variable,function name,method name,class name)
class name is a one type identifier


class ClassName:#classname first letter should be a uppercase.
    name="kishore"
    def display(self):
        name="abinaya"
        print(name)

#example:
    
class ClassName:
    pass



Object:
=======
instance of a class.

data call using class name:

classname.var;


class Class1:
    name="class 1"
    categery=5
    
#classname.var
print(Class1.name)
print(Class1.categery)

#create object
#obj=classname()

c=Class1()#c is a object var,it holds all instances of class1.
print(c.name)
print(c.categery)



class Human:
    name="savitha"


print(Human.name)#savitha
obj=Human()
print(obj.name)#savitha
obj.name="Elakkiya"
print(obj.name)#elakkiya
print(Human.name)#savitha



class Human:
    name="Abirami"
    def display(self):#self is declared defaultly.it hold object name(obj--self=h(obj))
        name="Deepika"
        print(name)#deepika
        print(self.name)#h.display=self.display#abirami


h=Human()
#obj.function()
h.display()

        

class Human:
    name1="Abirami"
    def display(self):
        name2="Deepika"#local var (use inside the function)
        self.name2=name2
        print(name2)#deepika
        print(self.name1)#abirami


h=Human()
h.display()
print(h.name1)#abirami
print(h.name2)#deepika



class Human:
    def getData(self):
        self.name=input("Enter name : ")
        self.gender=input("Enter Gender : ")
        
    def showData(self):
        print("name : %s  gender : %s"%(self.name,self.gender))

#create 6 object
h1=Human()
h2=Human()
h3=Human()
h4=Human()
h5=Human()
h6=Human()
#insert data
h1.getData()
h2.getData()
h3.getData()
h4.getData()
h5.getData()
h6.getData()
#display the data
h1.showData()
h2.showData()
h3.showData()
h4.showData()
h5.showData()
h6.showData()

"""

class Human:
    def getData(self,name,gender):#n1--->name,gen---->gender
        self.name=name
        self.gender=gender
        print(name,gender)#local var(name,gender)
        
    def showData(self):#when create a function inside class that is called method
        #print(name,gender)#local var(name,gender) can't access
        print("name : %s  gender : %s"%(self.name,self.gender))


n1=input("Enter name : ")
gen=input("Enter Gender : ")

h1=Human()
h1.getData(n1,gen)
h1.showData()


h2=Human()
h2.getData("Abirami","female")
h2.showData()

