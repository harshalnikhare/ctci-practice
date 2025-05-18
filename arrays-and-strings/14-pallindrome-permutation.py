"""
1.4
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input:
 Tact Coa
Output:
 True (permutations: "taco cat". "atco cta". etc.)
Hints: # 106, #121, #134, #136
"""


def pallindrome_permutation(str):
    dict = {}
    for char in str:
        if char == " ":
            continue
        elif char in dict:
            dict[char] += 1
        else:
            dict[char] = 1

    for key, value in list(dict.items()):
        if value % 2 == 0:
            del dict[key]

    if len(list(dict.keys())) % 2 == 0:
        return len(dict) == 0
    else:
        return len(dict) == 1


print(pallindrome_permutation("tact coa"))
print(pallindrome_permutation("harshal"))
