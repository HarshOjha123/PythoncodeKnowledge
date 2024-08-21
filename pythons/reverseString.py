def reverseString(s):
    a=""
    for i in s:
        a=i+a
    return a
s="geeksforgeeks"
print(reverseString(s))