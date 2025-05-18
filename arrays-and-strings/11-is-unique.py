"""
1.1
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, # 777, # 732
"""

# If no unique characters then O(n2)


def isUnique(str):
    strSet = set()
    for char in str:
        if char in strSet:
            return False
        else:
            strSet.add(char)
    return True


print(isUnique("harshal"))
print(isUnique("tesla"))
