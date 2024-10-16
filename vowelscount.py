def vowel_count(string):
    vowels = {}

    vowels_words = ['a','e','i','o','u','A','E','I','O','U']

    for i in string:
        if i in vowels_words:
            if i in vowels:

                vowels[i]+=1

            else:
                vowels[i] =1

    return vowels


string_word = "Ilovemycountry"

count_words = vowel_count(string_word)
print(count_words)



