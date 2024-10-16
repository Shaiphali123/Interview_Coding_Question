"""
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and unchangeable.

"""
tuple1 = ("Rectangle","Circle","Square")
print(tuple1)

"""
Find Duplicates in a List
"""
list1 = [2,3,4,5,6,7,8,2,6,5,4,6,6]
list2 = set(list1)
print(list(list2))

"""
input : list1 = [2,4,6,7,8,1,9]
tuple1 = ("a","f","t","w","d","e","t")
output : dict1 = {2:"a",4:"f",6:"t",7:"w"} 
"""

List1 = ["a","b","c","d","e","f"]
tuple1 = (1,2,3,4,5,6)

res = dict(zip(List1,tuple1))

print("The Dictinory is created", str(res))

"""
Convert list into tuple, set 
"""

List1 = [2,3,4,6,7,8,9,10,23,23,23, 56,45,56,56]
"""List2 = set(List1)
print(List2)

List3 = tuple(List2)
print(List3)"""

listtostring = "".join(map(str,List1))

print(listtostring)

"""
Convert tuple into the list,set,string
"""

tuple1  = (1,3,2,3,4,2,6,3,6,7,4,6)
#list1 = list(tuple1)
#print(list1)
#print(set(list1))

tupletostring = "".join(map(str,tuple1))
print(tupletostring)




