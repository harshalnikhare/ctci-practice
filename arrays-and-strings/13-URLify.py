"""
1.3
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input:
 "Mr John Smith
 "J
 13
Output:
 "Mr%20John%20Smith"
Hints: #53, #778
"""


def URLify(str):
    urlStr = ""
    for char in str:
        if char == " ":
            urlStr += "%20"
        else:
            urlStr += char
    return urlStr


print(URLify("Mr John Smith"))
