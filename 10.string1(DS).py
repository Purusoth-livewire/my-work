"""
#check
isupper()
islower()
isalnum()  #alphabet and number
isalpha()  #alphabet
isspace()
isdigit()
isnumeric()
isdecimal()


p=eval(input("Enter a data : "))

if p.isupper():
    print(p.lower())
else:
    print(p)


p=eval(input("Enter a data : "))

if p.islower():
    print(p.upper())
else:
    print(p)


p=eval(input("Enter your Password : "))
if p.isalpha():
    print("Password accepted...")
else:
    print("set ur password using only alphabet...")


p=input("Enter password : ")
if p.isdigit():
    print("password accepted.")
else:
    print("password not accepted.")


p=input("Enter password : ")
if p.isdecimal():
    print("password accepted.")
else:
    print("Password not accepted.")


p=eval(input("Enter password : "))
if p.isnumeric():
    print("password accepted.")
else:
    print("password not accepted")
"""
p="   "
if p.isspace():
    print("space allocated!")
else:
    print("space not allocated...")
