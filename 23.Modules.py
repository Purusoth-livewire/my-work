"""
Modules:
=========
modules(library function)---header file for other language

Other language header file:
===========================
stdio.h----printf(),scanf()
conio.h----getch(),clrscr()
string.h-----strcpy(),strlen(),strrev(),strcat()

#include<stdio.h>

python:

math
random

import math
"""
               
#import module_name
import math
print(math.pi)
print(math.e)
print(math.sin(0))
print(math.cos(0))


#import modulename as alias_name
import math as m
print(m.pi)
print(m.e)
print(m.sin(0))
print(m.cos(0))

#from module_name import function_name
from math import pi
print(pi)
#print(e)

#from module_name import function_name1,function_name2
from math import pi,e
print(pi)
print(e)

#from module_name import *   (call all function name )
from math import *
print(pi)
print(e)
print(sin(0))
