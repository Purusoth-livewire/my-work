"""
Recursion:
==========
function can call itself.



#normal function
def display():
    print("abirami")


display()#normal function call
display()
display()
display()
display()

"""

#recursion program
def disp(n):
    print(n)
    if n==1:
        return 1
    else:
        return disp(n-1)#recursive call



num=int(input("Enter a number : "))
disp(num)#function call
