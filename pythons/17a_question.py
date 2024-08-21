# example recursive 

def sumof(num):
    if num==0:
        return 0
    else:
        return sumof(num-1) + num
n=int(input("enter"))
print(sumof(n))

#pattern
p=int(input("no of row"))
def pattern(p):
    for i in range(p,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print('')    
s=pattern(p)

