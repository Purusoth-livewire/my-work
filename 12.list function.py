"""
list function:
==============

len()----count the total value in a list

data add:
=========
append()---add only one value in a list element
extend()---add multiple values in a list elements
insert()---add a value for particular position in a list 4element


copy()----copy the one list elements into another list
reverse()---reverse the list elements
sort()------ascending order

index()---find the values position
count()-----count the particular value

delete:
=======
pop()----erase last elements data
pop(index)----erase the particular position data in a list
remove(value)----erase the particular value
clear()------erase the elements in a list
del ref[index]----delete the index value
del ref-------delete the list


num=[1,2,3,10,4,10,5]
print("length : ",len(num))

print("num : ",num)
#obj_ref.append(value)

num.append(10)
print(num)

#obj_ref.extend([no. of values])
num.extend([12,13,14])
print(num)

#obj_ref.insert(index,value)
num.insert(0,100)
print(num)

print(num.index(13))

print(num)

num1=num.copy()
print(num1)

num1.reverse()
print(num1)

num1.sort()
print(num1)

print(num1.count(10))

print(num)

num.pop()
print(num)
num.pop(0)
print(num)


num.remove(10)
print(num)

del num[6]
print(num)

num.clear()
print(num)
del num
print(num)


list membership Test:
=====================

in
not in



list1=[1,2,3,4,5]

print(2 in list1)
print(2 not in list1)
print(6 not in list1)


list1=[1,2,3,4,5,6,7,8,9,10]

for i in list1:
    print(i)


list1=[1,2,3,4,5,6,7,8,9,10]
#1+2+3+4+5+6+7+8+9+10=?
sum=0
length=len(list1)
cnt=0
print("no. of values : ",length)
for i in list1:
    cnt+=1
    sum+=i
    if cnt!=length:
         
    else:
        print(i,end="=")
print(sum)
"""

#1+2+4+5+8+6+9+7+13=?
list1=[1,2,4,5,8,6,9,7,12]

length=len(list1)
cnt=0
sum=0
for i in list1:
    sum+=i  #sum=sum+i
    cnt+=1  #cnt=cnt+1
    if cnt!=length:
        print(i,end="+")
    
print(i,sum,sep="=")
