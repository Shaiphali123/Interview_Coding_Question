"""
Problem 2: Check if Two Strings Are Anagrams
Description:
Determine if two strings are anagrams of each other.
Two strings are anagrams if they contain the same characters in the same frequency but potentially in a different order.

Example:

Input: "listen", "silent"
Output: True

Input: "hello", "world"
Output: False
"""

def anagram(s1,s2):
    sorted(s1) == sorted(s2)

    if sorted(s1) == sorted(s2):
        print("This is Anagram")

    else:
        print("This is Not an Anagram")

anagram("listen","silent")
anagram("hello","world")

