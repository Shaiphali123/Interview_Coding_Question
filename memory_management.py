import sys

list1 = [1,2,3,4,5]
tuple1 = (1,2,3,4,5)
string = "shaiphali"
set = {2,3,4,5,6}
dictionary = {"a": 2, "b": 3, "c": 4}

print("the memory taken by the list is :" ,sys.getsizeof(list1),"bytes")
print("the memory taken by the tuple is :" ,sys.getsizeof(tuple1),"bytes")
print("the memory taken by the string", sys.getsizeof(string),"byte")
print("the memory taken by the string", sys.getsizeof(set),"byte")
print("the memory taken by the dictionary", sys.getsizeof(dictionary),"byte")


