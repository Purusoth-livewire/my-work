"""
Function:
=========
1.inbuild function
2.user defined fucntion

1. inbuild function:
====================
predefined function
to write set of code 

a=20
input()
int(10.2)
str()
float()
complex()
id()
eval()
print()---function

#sample program
m1=int(input("Enter mark 1 : "))
m2=int(input("Enter mark 2 : "))
m3=int(input("Enter mark 3 : "))


if m1>=0 and m1<=100:
    if m1>=40:
        print("mark 1 : pass")
    else:
        print("mark 1 : fail")
else:
    print("mark 1 : Invalid mark.")

if m2>=0 and m2<=100:
    if m2>=40:
        print("mark 2 : pass")
    else:
        print("mark 2 : fail")
else:
    print("mark 2 : Invalid mark.")

if m3>=0 and m3<=100:
    if m3>=40:
        print("mark 3 : pass")
    else:
        print("mark 3 : fail")
else:
    print("mark 3 : Invalid mark.")
    


user defined function:
========================
self contained programming structure

code reuse

#1.function without arguments and without return type
syntax
======
def functionname():
    '''doc string'''
    statements

functionname()


#program1 
def result():
    '''conguarations...'''#documentation string
    mark=int(input("Enter mark : "))
    if mark>=0 and mark<=100:
        if mark>=40:
            print("Result : pass")
        else:
            print("Result : fail")
    else:
        print("mark : Invalid entry...")


result()
result()
result()
result()
result()
result()
print(result.__doc__)#functionname.__doc__


#program2

def add():
    a=int(input("Enter a value : "))
    b=int(input("Enter a value : "))
    c=a+b
    print("add : ",c)

add()


#2.Function with arguments and without return type

syntax:

def function(ref):
    '''docstring'''
     statements

fucntion(value)


def add(a,b,c):
    add=a+b+c
    print("add : ",add)


add(12,13,68)
v1=23
v2=34
v3=23
add(v1,v2,v3)#a=v1,b=v2

#Function with Arguments
=========================
1.positional arguments
2.Default arguments
3.keyword arguments
4.variable length arguments or arbitary arguments



#1.positional arguments
def greet(a,b):#a="abirami"  b="Elakkiya"
    print("Happy birthday! ",a)
    print("Happy birthday! ",b)

greet("abirami","Elakkiya")

#default arguments
#def greet(name,msg="happy birthday!"):
def greet(name,msg="happy birthday!"):
    print(msg,name)

greet("abirami")
greet("Elakkiya")


#3.keyword arguments

def show(a,b,c=12):
    print(a,b,c)
show(a=10,b=20)
show(a=11,b=3,c=5)
show(2,7)
show(4,6,5)
show(c=23,a=45,b=33)


#4.Arbitary or variable length arguments

def chennaisilks(name,*product):
    print("Bill name : ",name)
    print("your products are ")
    for i in product:
        print(i)
        

chennaisilks("abirami","chudi","saree")
chennaisilks("Elakkiya","jeans","T-shirt","shirts")
chennaisilks("divya","bangal","hairpins","neil polish","lipstick","hand bag","hand mirror","perfume","glass")


#3.Function without argument with return type:

Syntax:

def function():
    statements
    return
a=function()


def add():
    a=int(input("Enter value 1 : "))
    b=int(input("Enter value 2 : "))
    c=a+b
    return c

c=add()
print(c)


print(add())


#4.function with arguments & with return type:


syntax:

def funtcion(var):
    statements
    return

var=function()

"""

def add(a,b):
    c=a+b
    return c

c=add(10,5)
print(c)
