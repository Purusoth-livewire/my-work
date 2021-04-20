"""
control flow:
=============
1.Decision making
2.looping structure

1.Decision making:
==================
1.if statements
2.if-else statements
3.elif statements
4.nested if-else statements


if -statements:
================
condition is true,it will true statements
syntax for other language:
==========================
if(condition)
{
  statements
}

syntax for python:
==================
if condition:
    statements
    statements


#pgm1
s1=int(input("Enter mark : "))
s2=int(input("Enter mark : "))

if s1>s2:
    print("student 1 is Topper.")


if-else staements
=================
if the condition is true, it will excutes true(if) statements.
if the condition is false, it will excutes false(else) statements.

syntax:
=======

if condition:
    statements
else:
    statements


s1=int(input("Enter s1 mark : "))
s2=int(input("Enter s2 mark : "))

if s1>s2:
    print("student 1 is Topper.")
else:
    print("Student 2 is Topper.")


if-elif-else statements:
========================
syntax:
=======
if condition1:
    statements
elif condition2:
    statements
elif condition3:
    statements
else:
    statements

s1=int(input("Enter s1 mark : "))
s2=int(input("Enter s2 mark : "))

if s1>s2:
    print("student 1 is Topper.")
elif s1<s2:
    print("Student 2 is Topper.")
else:
    print("student 1 & student 2 are Toppers.")


Netsed if-else statements:
==========================

syntax:
=======

if condition:
    if condition:
        statements
    else:
        statements
else:
    if condition:
        statement
    else:
        statements


s1=int(input("Enter student 1 mark : "))
s2=int(input("Enter Student 2 mark : "))
s3=int(input("Enter Student 3 mark : "))

if s1>s2:
    if s1>s3:
        print("student 1 is Topper.")
    else:
        print("student 3 is Topper.")

else:
    if s2>s3:
        print("Student 2 is Topper.")
    else:
        print("Student 3 is Topper.")
    
"""
#smallest among 2 numbers?
#smallest among 3 numbers?
#find given number is odd or even?


#find given year is leap year or not?

year=int(input("Enter a year : "))

if year%4==0:
    print(year,"is leap year.")
else:
    print(year," is not leap year")
