"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
Hints: #92, # 11 0
"""


def string_compression(string):
    if len(string) == 0:
        return ""
    cStr = string[0]
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            cStr += str(count)
            cStr += string[i]
            count = 1
    cStr += str(count)

    return cStr


print(string_compression("aabcccccaaad"))
