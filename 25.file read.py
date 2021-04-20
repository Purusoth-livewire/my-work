"""
read to file:
=============
file -----> program

syntax:
=======
var=open("path,filename","r")

var.read()
var.readline()
var.readlines()

#program1

f=open("demo.txt","r")
print(f.read())#display output 
f.close()


#program2
f=open("demo.txt","r")
print(f.readline())#display output for line by line
print(f.readline())
print("current position of cursor : ",f.tell())
print("change cursor position : ",f.seek(5))#syntax : var.seek(position number)
print("current position of cursor : ",f.tell())
print(f.readline())
print(f.readline())
f.close()

#program 3

f=open("demo.txt","r")
print(f.readlines())#display output for line by line
f.close()

#program 4

f=open("demo.txt","r")
for line in f.readlines():
    print(line)
f.close()


"""
#program 5

f=open("demo.txt","r")
print(f.read(50))
#display output for first 50 character    syntax: f.read(no. of character)
f.close()
