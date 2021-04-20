"""
Tuple:
======
tuple is like a list.
store the multiple data items.
ordered collection of object

tuple immutable-----can't modify
Tuple is accessed by index.
length was fixed.

syntax:
=======
ref=(no of elements)
"""
empty=()
print(empty)

t=(1,2,3,4,5,6)
print(t)
#positive index
t=(1,"abirami","Elakkiya")
print(t)
print(t[0])
print(t[1])
print(t[2])
#negative index
t=(1,2,3,4,5)
print(t[-5])
print(t[-4])
print(t[-3])
print(t[-2])
print(t[-1])
#used tuple in a list:
t=(1,2,[3,4,5])
print(t[2])
print(t[2][1])
#concatenate(+) two tuple(join)
t1=(1,2,3)
t2=(5,7,8)
t3=t1+t2
print(t3)
#repeatation(*) the tuple value
t1=(1,2,3)
t2=3*t1#1,2,3,1,2,3,1,2,3
print(t2)
"""
Tuple function:
===============
count(value)
index(value)

len()
max()
min()
sorted()
sum()
"""
print(t2.count(2))
print(t2.index(3))

print(len(t2))
print(max(t1))
print(min(t1))

t1=(2,6,4,9,8,3,2)
print(sorted(t1))
print(sum(t1))

"""
Tuple Membership Test:
======================
in
not in
"""

t1=(1,3,2,6)
print(2 in t1)
print(2 not in t1)
print(7 in t1)
print(7 not in t1)

