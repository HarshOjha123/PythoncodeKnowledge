'''A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.'''
#python has in nuilt package "re" for regular expression

import re
x="he is a very good boy and he loves playing cricket"
y=re.search("is a very",x)
if y:
    print("yes")
else:
    print("no")
#if no match found it returnse None    
#there are four functions in re for pattern searching in string
''' 1)search() = The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned    
2)The findall() function returns a list containing all matches    
3)The split() function returns a list where the string has been split at each match
4)The sub() function replaces the matches with the text of your choice'''

z=re.findall("ve",x)
print(z)
#if no match founds return empty list[]

h=re.split("i",x)
print(h)

i=re.sub("i","j",x)
print(i)

'''A Match Object is an object containing information about the search and the result.
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match'''

g="india is my country"
o=re.search(r"\bm\w+",g)
print(o.span())
p=re.search(r"\bi\w+",g)
print(p.group())