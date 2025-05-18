"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale,
 pIe
 -> true
pales. pale -> true
pale.
 bale
 -> true
pale.
 bake
 -> false
Hints: #23, #97, #130
"""


def one_away(str1, str2):
    dict = {}
    for char in str1:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for char in str2:
        if char in dict:
            dict[char] -= 1

    for key, value in list(dict.items()):
        if value == 0:
            del dict[key]

    if len(dict) == 1 and list(dict.values())[0] <= 1:
        return True

    return False


print(one_away("pale", "ple"))
print(one_away("pales", "pale"))
print(one_away("pale", "bale"))
print(one_away("pale", "bake"))
