vowels_element = input("Enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowels_present = []
consonents_present = []

for i in vowels_element:
    if i in vowels:
        vowels_present.append(i)
        print(f"the vowel is '{i}' present")


    else:
        consonents_present.append(i)
        print(f"the consonents is '{i}' present")

print(vowels_present)
print(consonents_present)