"""
Constructor:
============
when create a object for class it will execute automatically.
no need to call the function.
__init__()---->constructor

#program1

class Human:
    def __init__(self):#constructor
        print("Human class constructor called")
    def show(self):
        print("Human class show function called")



h=Human()#create a object
h.show()


#program2

class Human:
    def __init__(self):#constructor
        self.name=input("Enter name : ")
        self.age=int(input("Enter age : "))
    def showDetails(self):
        print("name : ",self.name)
        print("age : ",self.age)


h=Human()
#h.getDetails()
h.showDetails()


#program3:


class Human:
    def __init__(self,name, age):#constructor
        self.name=name
        self.age=age
    def showDetails(self):
        print("name : ",self.name)
        print("age : ",self.age)


h1=Human("deepika",19)
h1.showDetails()
h2=Human("Boomika",19)
h2.showDetails()


