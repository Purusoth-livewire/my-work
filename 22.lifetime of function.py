"""
lifetime & scope of variable:
=============================

"""
#program1
def show():
    global a
    print(a)
    a=20
    print(a)

a=10
print(a)
show()
print(a)
