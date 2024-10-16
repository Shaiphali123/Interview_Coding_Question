"""
Given a string, find the first non-repeating character. If there are no non-repeating characters, return None.
Example:
Input: "swiss"
Output: "w"
Input: "repeater"
Output: "a"
"""

"""
Explanation:
Count Characters:

Use a dictionary char_count to store the number of occurrences of each character.
Find Non-Repeating Character:

Iterate through the string a second time to find the first character with a count of 1.

"""
def first_non_repeating_char(s: str) -> str:
    char_count = {}

    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char

    return None


# Example usage:
print(first_non_repeating_char("swiss"))  # Output: "w"
print(first_non_repeating_char("repeater"))  # Output: "a"



