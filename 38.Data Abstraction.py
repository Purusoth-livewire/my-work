"""
Data Abstraction:
=================
it can provide only essential Information.
Data  Hiding.

"""

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

obj=Human()
obj.showDetails
