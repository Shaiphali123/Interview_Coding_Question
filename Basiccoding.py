# 1. Check String is palindrom or not
def palindrom(num):
    num1 = num[::-1]

    if num == num1:
        print("Number is palindrom")

    else:
        print("Number is not Palindrom")


num = "radar"
palindrom(num)


# 2. Reverse a String
# eg :Str  = "Python"
# reverse String is "nohtyP"

def functionstring(name):
    name1 = name[::-1]

    print("Reverse String is :", name1)


name = "Shaiphali"
functionstring(name)


# 3. Reverse a words
# eg: Str = "This is My Country"
# Output Should be str = "Country My is This"
# Trip: string -> List(split) -> reverse(reverse) -> string(join)
def reverseword(word):
    list1 = word.split()
    list1.reverse()

    list2 = " ".join(list1)

    print(list2)


word = "This is My Country"
reverseword(word)


# 4. remove the Duplicate String
# I/P "Shhbhklldkkkkjjhdhfkkk"
# O/P "shbkldjf"

def Duplicatestring(string1):
    List1 = []

    for i in string1:
        if i not in List1:
            List1.append(i)

    print(List1)

    list2 = "".join(List1)
    print(list2)


string1 = "Shhbhklldkkkkjjhdhfkkk"

Duplicatestring(string1)


# 5. Find the Fibonacci Series
# if n <= 0 ; return 0
# if n == 1 ; return 1
# if n >1 ; return Fn-1 + Fn-2

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)


print(Fibonacci(9))
