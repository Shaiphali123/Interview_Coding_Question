"""
Lists are used to store multiple items in a single variable.
Lists are one of 4 built-in data types in Python used to store collections of data,
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
Lists are created using square brackets:
Lists are orderable, changable, allow duplicate element
"""

list1 = ["apple", "mango", "Cherry"]
print(list1)
# access element in the list

print(list1[1])

# add element in the list by append function
list1.append("Litchi")
print(list1)
# add element in the list by the index value
list1[3] = "banana"
print(list1)

print(list1.pop())
print(list1.pop(2))

list1.append("apple")
print(list1)

# Loop List
list2 = [2,5,5,9,3,5,6,9]
for i in list2:
    print(i)

for i in range(len(list2)):
    print(i)

# list Comphrehension
[print(i) for i in list2]

