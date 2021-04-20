"""
Looping Structure:
==================
set of statements continuously done untill condition fails.

steps:
======
1.initialize
2.condition
    true
    3.statements
    4.update
    5.back to step 2
6.false---exit the loop



loop:
=====
1.indefinite loop(loop never end)
2.definite loop(loop will end )

indefinite loop:
================
loop never end.

while True:
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    if age>18:
        print(name," is eligible to vote.")
    else:
        print(name," is not eligible to vote.")
    
program2:
=========
i=1
while i<=3:
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    if age>18:
        print(name," is eligible to vote.")
    else:
        print(name," is not eligible to vote.")

2.definite loop:
================

#program1
i=1
while i<=3:
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    if age>18:
        print(name," is eligible to vote.")
    else:
        print(name," is not eligible to vote.")
    i+=1#i=i+1



#program2:print 1 to 10

i=1
while i<=10:
    print(i,end="  ")
    i+=1


#program3:print 1 to n number

n=int(input("Enter End number : "))
i=1
while i<=n:
    print(i,end="  ")
    i+=1


#program4: print n number to 1

#program5: sum of series  1+2+3+4+5+6+7+8+9+10=55

i=1
sum=0
while i<10:
    print(i,end="+")
    sum+=i
    i+=1
sum+=i
print(i,sum,sep="=")


#program6 : sum of series 1+4+9+16+25+36+49+64+81+100=?

num=int(input("Enter end number : "))
i=1
sum=0
while i<num:
    square=i*i
    sum+=square
    print(square,end="+")
    i+=1
square=i*i
sum+=square
print(square,sum,sep="=")


#program7: sum of series  1-2+3-4+5-6+.........+n=?

num=int(input("Enter end number : "))
i=1
odd=0
even=0
while i<num:
    if i%2==0:
        print(i,end="+")
        even+=i
    else:
        print(i,end="-")
        odd+=i
    i+=1
if i%2==0:
    even+=i
else:
    odd+=i
sum=odd-even
print(i,sum,sep="=")


#program 8: reverse number i/p--1234  o/p--->4321

num=int(input("Enter a number : "))
n1=str(num)
print("output : ",end="")
print(n1[::-1])


#program 9:reverse a name  i/p---"abirami"  o/p---"imariba"

name=input("Enter name : ")
print("Reverse name : ",end="")
print(name[::-1])
"""

#program 10:palindrome
