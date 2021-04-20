"""
Data Encapsulation:
===================
Wrapping up to information.
Ex:class
secure the data.


class Human:
    def __init__(self):
        self.name=input("Enter name : ")
        self.fname=input("Enter Father name : ")
        dob=input("Enter Date of Birth : ")
        age=int(input("Enter age : "))
        Address=input("Enter Address")
        self.mobile=input("Enter mobile number : ")
        print("Your data inserted successfully....")
    def showDetails(self):
        print("name of student : ",self.name)
        print("mobile : ",self.mobile)
"""



class Encapsulation:
    data1=25#public var--->it can use anywhere of the program(own class,new class,main)
    __data2=50#private var---cant use outside the class(own class)
    def showDetails(self):
        print("Data1 : ",self.data1)
        print("Data2 : ",self.__data2)
        self.data1=10001
        data1=50
        __data2=100
        self.__data2=100
        print(data1,__data2 )
        print("Data1 : ",self.data1)
        print("Data2 : ",self.__data2)


obj=Encapsulation()
obj.showDetails()
print(obj.data1)
#print(obj.__data2)
