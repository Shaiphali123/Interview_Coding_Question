def char_count(string,char):
    count = 0
    for i in string:
        if i == char:
            count+=1

        return count

string_count = input("Enter the String :")
char_to_count = input("Enter the character to count: ")

count = char_count(string_count,char_to_count)
print(f"The character '{char_to_count}'is '{count}")

# WAP to store result in dictionary

def char_count(string):
    dict1 = {}
    for i in string:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
        return dict1

string_count = input("Enter the String")
count = char_count(string_count)
print(count)