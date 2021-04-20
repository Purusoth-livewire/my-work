"""
Dictionary:
===========
dictionary is unorder collection of items.
key:value pair

value accessed by key.
key----mutable(can't modify)
value---immutable(modify)

syntax:

ref={key1:value,key2:value2}
"""
d={1:"abirami",2:"Elakkiya"}
print(d)
#ref[key]
print(d.keys())
print(d.items())
print(d.values())

print(d[1])
print(d[2])


d={"name1":"abirami","age1":"20","name2":"Elakkiya","age2":20}
print(d)

print(d["name1"])
d["name1"]="divya"
print(d["name1"])
print(d)

#add elements
d["mob1"]=9952440707
d["mob2"]=6385827027
print(d)

#access the elements
print(d.get("mob1"))
print(d["mob2"])

#del the item
#ref.pop(key)
print(d.pop("name1"))#erase and display erased data
print(d)

#ref.popitem()
print(d.popitem())#erase last data and display it 

print(d.clear())

del d

d1={1:"divya"}
print("d1 :",d1)
d2={}
d2=d1.copy()
print("d2 : ",d2)
