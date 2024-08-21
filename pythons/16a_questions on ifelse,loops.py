# practice set codewith harry
# Q1
'''a=int(input("enter the a sub no."))
b=int(input("enter the b sub no."))
c=int(input("enter the c sub no."))
d=((a+b+c)/300)*100
print(d)
if d>40:
    if c>33 and b>33 and a>33:
        print("pass")
    else:
        print("fail")'''

# Q2

'''mesg=input('enter the msg')
if "make a lot of money" in mesg:
    print("spam")
elif "buy now" in mesg:
    print("spam") 
elif "subscribe this" in mesg:
    print("spam")
else:
    print(mesg)'''           


# loop questions

'''n=int(input("enter the number"))
i=1
while i<11:
    print(str(n) + "x" + str(i) + "=" + str(n*i))
    i+=1'''

# Q2
    
'''list=["harsh","rahul","ram","rakesh"]
for x in list:
    if x.startswith("r"):
        print(x + " " + "ojha")'''
# Q3

'''n=int(input())
for i in range(2,n):
    if n%i==0:
        print("not a prime no")
        break
else:
    print("prime no.")'''
    
# Q4
'''n=int(input())
i=1
sum=0
while i<n+1:
    sum+=i
    i+=1
print(sum)'''

# Q5

'''n=int(input())
fact=n
factorial=1
for i in range(1,n+1):
    factorial=factorial*i 
print("factorial of" + " " + str(fact) + "=" + str(factorial))'''         
        
#Q6 to print right angle pyramid

'''n=int(input("enter no of row:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()'''
    
#Q7 reverse right angle pyramid

'''rows = int(input("Enter the number of rows:"))  
k = 2 * rows - 2  # It is used for number of spaces  
for i in range(0, rows):  
    for j in range(0, k):  
        print(end=" ")  
    k = k - 2   # decrement k value after each iteration  
    for j in range(0, i + 1):  
        print("* ", end="")  # printing star  
    print("")'''
      
#Q8 full pyramid
     
'''n=int(input("enter the no. of rows"))
m=(2*n)-2
for i in range(0,n):
    for j in range(m):
        print(end=" ")
    m-=1
    for j in range(0,i+1):
        print("*",end=" ")    
    print("") 
#n=int(input("enter the no. rows"))
#m=(2*n)-2
m=n-2
for i in range(n,-1,-1):
    for j in range(m,0,-1):
        print(end=" ")
    m+=1
    for j in range(0,i+1):
        print("*",end=" ")
    print(" ")'''    
#9    
    
'''n=int(input())
for i in range(0,n+1):
    for j in range(n-i,0,-1):
        print(str(j) + " " ,end=" ") 
    print("")'''    

#Q10 square pattern

'''n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print(str(i),end=" ")
        else:
            print(j,end=" ")
    print()'''

#Q11

#n=int(input())
'''for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ") 
    print()''' 
'''for i in range(0,n):
    for j in range(0,i+1):    
        print("*",end=" ")
    print()'''     
            