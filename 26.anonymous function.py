"""
anonymous or lambda function:
=============================
create function without using "def" keyword
it is a one line function
use multiple lambda variable but do only one expression

syntax:
========

var = lambda func_var:expression


#program 1:

#normal function
def func1(n):
    ans=2**n
    return ans

ans=func1(2)
print("func 1 : ",ans)

#lambda function
func2=lambda power : 2**power
print("func 2 : ",func2(2))



#program2
func=lambda x:x+x

n=int(input("Enter a number : "))
a=func(n)
print(a)


#program3

func=lambda a,b,c:a+b+c


a=int(input("Enter value 1 : "))
b=int(input("Enter value 1 : "))
c=int(input("Enter value 1 : "))
ans=func(a,b,c)
print(ans)


inside the lambda function we can done two function
1.filter
2.map

1.filter:
=========
filter a particular values in a list

syntax:
filter(lambda var: expression,list1)
ex
new_list=list(filter(lambda var:expression,list))


#program 5
old_list=[89,78,45,34,90,19,5,18,6,13]
#print pass mark in this list using lambda filter function

new_list=list(filter(lambda x:x>=40,old_list))
print(new_list)


2.map:
======

map(lambda var:expression,list)
ex:
new_list=list(map(lambda var:expression,list))
"""

old_list=[89,78,45,34,90,19,5,18,6,13]
newlist=list(map(lambda x:x/4,old_list))
print(newlist)


