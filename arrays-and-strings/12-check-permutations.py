"""
1.2
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737
"""


def check_permutations(str1, str2):
    dict = {}
    for char in str1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char in str2:
        if char in dict:
            dict[char] -= 1
        else:
            return False

    for value in dict.values():
        if value != 0:
            return False
    return True


print(check_permutations("harshal", "narshalr"))
print(check_permutations("harshal", "hhaasrl"))
