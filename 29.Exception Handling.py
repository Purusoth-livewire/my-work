"""
Exception handling:
===================
exception occurs(logical error)------>raise the exception(try)---->catch(except)
try,except,else,finally,raise


try:
====
write a code to find errors .
It will checks the errors occurs in the program or not.
if the error occurs during the program try will throw the exception in except block.

try:
    code

except:
=======
    display the information after exception what we do.

except exception_name:
    statements

else:
=====
if there is no exception that the time it will excutes else block.

else:
    statements

finally:
========
dont care about program

if the have to occurs  errors or not
it will done this process

finally:
   statements

raise:
======
raise the exception
"""

try:
    a=int(input("Enter value : "))
    if a==0:
        raise ZeroDivisionError
    elif a==10:
        raise AssertionError
    else:
        pass    

except AssertionError:
    print("enter correct data")
except NameError:
    print("give profer name")
except ZeroDivisionError:
    print("give divident value above zero")
except BaseException:
    print("something wrong! check ur program...")

else:
    c=10/a
    print("ans : ",c)
    #print("password accepted successfully!")

finally:
    print("program completed")
