def char_count(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1

    return dict1

string_count = input("Enter the String: ")
count = char_count(string_count)
print(count)

def count_string(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] +=1
        else:
            dict[i] = 1

    return dict1

string_count = input("Enter theNumber")
string = count()