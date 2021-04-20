destructor:
===========
Inverse of constructor.
automatically destroy the object.

in python we have automatic carbage collection mechanism.
so we dont need to write code neccessary.
but if you think write it is posiible.

__del__()

call destructor: del obj_name
"""

class Human:
    def __init__(self):
        self.name="Livewire"
    def showDetails(self):
        print("name : ",self.name)
    def __del__(self):#destructor
        self.name="no name"
        print("name : ",self.name)
        
h=Human()
h.showDetails()
del h#call Destructor
