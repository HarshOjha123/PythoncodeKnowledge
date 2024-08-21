#if syntax
from this import d


a=7
b=9
if a<b:
    print("a is less than b")
    
# nested if 
c=10
g=12
d=1546
if c<g:
    print("g is greater than c")
    if g<d:
        print("d is greatest") 
        
#if else
if a>b:
    print("b is less than a")
else:
    print("a is less than b")  
    
#elif statement
h=10
i=10
if h<i:
    print("h is smaller than i")
elif h==i:
    print("h is equal to i")
else:
    print("h is greater than i")                

#short if and short if else
#sigle line=ternary operators,conditional expressions\

f=999
k=888
print("f is > k") if f>k else print("k is > f")   
