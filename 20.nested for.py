"""
#program1 
for i in range(1,6):
    for j in range(1,6):
        print(i,j,sep="",end="  ")
    print()

#program2
for i in range(1,6):
    for j in range(5,0,-1):
        print(i,j,sep="",end="  ")
    print()

#program3
for i in range(5,0,-1):
    for j in range(1,6):
        print(i,j,sep="",end="  ")
    print()


#program4
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,j,sep="",end="  ")
    print()

#program5
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *
*  *  *  *  *

#program6
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
1  2  3  4  5
"""
for i in range(1,6):#outer loop----row
    for j in range(1,6):#inner loop---column
        print(j,end="  ")
    print()
"""
#program7
1  1  1  1  1
2  2  2  2  2
3  3  3  3  3
4  4  4  4  4
5  5  5  5  5


#program8

for i in range(1,6):
    for j in range(1,i+1):
        print(i,j,sep="",end="  ")
    print()

#program9

*
*  *
*  *  *
*  *  *  *
*  *  *  *  *

#program 10:
1
1  2
1  2  3
1  2  3  4
1  2  3  4  5

#program11
1
2  2
3  3  3
4  4  4  4
5  5  5  5  5

#Program12

for i in range(1,6):
    for j in range(1,6-i+1):
        print(i,j,sep="",end="  ")
    print()
"""
