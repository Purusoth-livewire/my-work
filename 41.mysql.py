"""
Database connectivity:
======================
database---record

file ----> program output data will be stored in notepad

database--->create ,modify,delete


sql,mysql,oracle

front end :  program(log in page)
back end  :  storage(mysql)



#program1--->mysql to python connection
import mysql.connector

sql_connect=mysql.connector.connect(host="localhost",user="root",password="12345")
#host--->system name(mysystem(localhost))
#user--->mysql name---root(default)
#password--->mysql password(installed time set=1234)
print("mysql to python connected successfully...")
sql_connect.close()



#program 2
#database creation

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="12345")
print("mysql connected...")

qry=con.cursor()#cursor ---> make all changes
qry.execute("create database vsb")#write a query
print("database is created...")

qry.close()

con.close()

#program3
#display database in mysql

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="12345")
print("mysql connected...")
qry=con.cursor()
qry.execute("show databases")
for db in qry:
    print(db)

print("database displayed successfullly...")
qry.close()
con.close()


#program4
#create table

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="12345",database="vsb")
print("mysql connected...")
qry=con.cursor()

qry.execute("create table student (s_no int,name varchar(50))")
print("table created successfully...")

qry.close()
con.close()

"""
#program5
#add column

import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="12345",database="vsb")
print("mysql connected...")
qry=con.cursor("show tables")

for db in qry:
    print(db)

qry.execute("")
print()

qry.close()
con.close()
