"""
file concept:
=============
whenever  i run a print() that the time the output data stored tempararely.(RAM)

program data stored permanently using harddisk.

program data----> documents(notepad)


steps:
======
1.create/open a file.
2.Perform the tasks
3.close the file.



1.create/open a file:
=====================
var=open("path,filename","mode")

path===>location(where it is stored)
mode===>write,append,read

ex:
===
f=open("file.txt","w")
f=open("e:\\file.txt","w")


3.close the file:
=================
var.close()
ex:
==
f.close()

2.perform tasks:
=================
#write
#append
#read

#write:
=======
program data to store file.
program data ---> file

syntax:
=======
var.write("prompt")


#program1
f=open("demofileconcept.txt","w")
f.write("Abirami\n")
f.write("Elakkiya\n")
f.close()


#program2

name1=input("Enter name 1 : ")
name2=input("Enter name 2 : ")
age1=input("Enter age 1 : ")
age2=input("Enter age 2 : ")

f=open("demofileconcept.txt","w")
#print(name1)
f.write("\nname : ")
f.write(name1)
f.write("\nage : ")
f.write(age1)
f.write("\nname : ")
f.write(name2)
f.write("\nage : ")
f.write(age2)

f.close()

append from a file:
===================
whenever i write a file using write mode.
just store that program data
previous data will be erased.
program data----(new data store and old data erase)

i need store that data also using append mode
just change mode to "a"
"a"---> append

program data----> old data+new data

var=open("path,filename","append")

path===>location(where it is stored)
mode===>append

ex:
===
f=open("file.txt","a")
f=open("e:\\file.txt","a")
"""


#program2

name1=input("Enter name 1 : ")
name2=input("Enter name 2 : ")
age1=input("Enter age 1 : ")
age2=input("Enter age 2 : ")

f=open("demofileconcept.txt","a")
#print(name1)
f.write("\nname : ")
f.write(name1)
f.write("\nage : ")
f.write(age1)
f.write("\nname : ")
f.write(name2)
f.write("\nage : ")
f.write(age2)

f.close()
