"""
#value=[1,4,6,9,3,0,2]
value=[1,3.14,"Abirami","Elakiya"]
print("list : ",value)
#positive indexing
print("value[0] : ",value[0])
print("value[1] : ",value[1])
print("value[2] : ",value[2])
print("value[3] : ",value[3])
#negative indexing
print("value[-1] : ",value[-1])
print("value[-2] : ",value[-2])
print("value[-3] : ",value[-3])
print("value[-4] : ",value[-4])

num=[1,2,3,[5,6,7]]
print("num : ",num)
print("num[0] : ",num[0])
print("num[1] : ",num[1])
print("num[2] : ",num[2])
print("num[3] : ",num[3])
print("num[3][0] : ",num[3][0])
print("num[3][1] : ",num[3][1])
print("num[3][2] : ",num[3][2])

#negative Indexing
print("num[-1][-1] : ",num[-1][-1])
print("num[3][-1] : ",num[3][-1])
print("num[-3] : ",num[-3])


num=[1,2,[3,4,[5,6]]]
print("num : ",num)
print("num[0] : ",num[0])
print("num[1] : ",num[1])
print("num[2] : ",num[2])
print("num[2][0] : ",num[2][0])
print("num[2][2][0] : ",num[2][2][0])
print("num[2][2][1] : ",num[2][2][1])

slicing:
========

"""
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#slicing operator---  :
print("num : ",num)
print("num : ",num[:])
#var[start index:]
print("num : ",num[5:])
#var[:end index]
print("num : ",num[:10])
#var[start index:end index]
print("num : ",num[5:10])


