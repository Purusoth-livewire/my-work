"""
Set:
====
unorder collection of item
set is immutable----modify the data
duplicate data are not allowed
it will display the data for randomly.
it can't access the data using index(offset).


list1=[1,2,3,1,2]
print("list data are : ",list1)
set1={1,2,3,1,2}
print("set data are : ",set1)
set2={78,32,45,22,56,99,100,0,199}
print("set value are ",set2)


set methods:
============
add()
update()

discard()
remove()
pop()
clear()


s={1,2}
print(s)
s.add(4)
print(s)
s.update([5,8,3,4])
print(s)

s.discard(8)
print(s)
s.discard(8)#already removed data gave here,result return no error

s.remove(5)
print(s)
#s.remove(5)#already remove data gave here,result return "keyerror"

s.pop()
print(s)

s.clear()
print(s)


set functions:
==============
len()
min()
max()
sum()
sorted()

s={1,4,2,7,8}
print(s)
length=len(s)
print("length : ",length)
m=max(s)
print("max : ",m)
m=min(s)
print("min : ",m)
s1=sum(s)
print("sum : ",s1)
s1=sorted(s)
print(s1)
print(s1[1])



set operations:
===============

set union
=========
use or(|) operator
use union operation


a={1,2,3,4,5}
b={4,5,6,7,8}
#use | operator
print(a|b)
print(b|a)
#output: (a|b == b|a)

#use union operator
#syntax:    var1.union(var2)
print(a.union(b))
print(b.union(a))



set intersection:
=================
#use and(&) operator
#use intersection operation


#and operator
a={1,2,3,4,5}
b={4,5,6,7,8}

print(a&b)
print(b&a)
#output : (a&b == b&a)


#intersection operation
#syntax----> var1.intersection(var2)

print(a.intersection(b))
print(b.intersection(a))



set difference:
===============
use (-)operator
use difference operation


#use (-) operator

a={1,2,3,4,5}
b={3,4,5,6,7}

print("a-b : ",a-b)
print("b-a : ",b-a)

#output : (a-b != b-a)

#set difference
#syntax :   var1.difference(var2)
print("a-b : ",a.difference(b))
print("b-a : ",b.difference(a))


set symmetric difference:
=========================
#use (^) operator
#use symmetric_difference operation

"""

a={1,2,3,4,5}
b={3,4,5,6,7}

#use (^) operator
print(a^b)
print(b^a)

#use symmetric_difference
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
