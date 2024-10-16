# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
list1 = [1,4,6,9,3,2]
f = 0
s = 0

for i in list1:
    if i > f:
        s = f
        f = i
    elif i < f and s < i and s < f:
        s = i

print(f, s)

list1 = [5, 5, 4, 3, 2, 1]
f = 999999999
s = 999999999

for i in list1:
    if i < f:
        s = f
        f = i
    elif i > f and s > i and s > f:
        s = i

print(f, s)