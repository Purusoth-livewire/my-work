"""
for loop:
=========

#syntax1:
#for var in range(end)


for i in range(11):#11-1=10
    print(i,end="  ")


#syntax2:
#for var in range(start,end)


for i in range(1,11):
    print(i,end=" ")


#syntax3:
#for var in range(start,end,update)
##start=1
#end=10-1=9
#inc=2,4

for i in range(1,11,2):
    print(i,end=" ")


for i in range(1,11,3):
    print(i,end=" ")


for i in range(10,0,-1):
    print(i,end=" ")

    
#syntax:
#for var in list:

for i in "abirami":
    print(i)



list1=[2,5,3,1,8,7,6]
for i in list1:
    print(i)


num=int(input("Enter end value : "))
sum=0
for i in range(1,num):
    sum+=i
    print(i,end="+")
sum+=num
print(num,sum,sep="=")

#display even number
for i in range(1,11):
    if i%2==0:
        print(i)

"""

#sum of digits 1234=1+2+3+4=10
num=int(input("Enter a number : "))#1234
sum=0
for i in str(num):
    #print(i)
    n1=int(i)
    sum+=n1
    
print(sum)
