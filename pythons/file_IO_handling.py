from asyncore import read
'''f=open('05_var.py','r')
p=f.read()
print(p)
f.close()'''
#p=f.read(5)# 5 represents the no. of words
#print(p)
#f.close()

#readline funstion is used to read one line 
'''p=f.readline()
print(p)

#reads the second line and so on.

p=f.readline()
print(p)'''
#different modes of opening a file
#1 read("r")

#2 write("w")
'''f=open("another.txt","w") #a file is created if it is not present in write mode for example this code generates new file with the name another.txt
f.write("i got 7.14 sgpa")#writes the content of " " in file
f.close()'''

#3 append("a") - is used to add content at the end in the file

'''f=open("another.txt","a")  
f.write(" and i am not happy")
f.close()'''

#4read and write("+")
'''
f=open("another.txt","w+")
f.write(",i should have got more no.s but my hand writing sucks")
p=f.read()
print(p)
f.close()
'''

#use of = with open ''syntax''
#with open("  "," ") as f

with open("another.text","w")as p:
    p.write("motherfucker fuckoff")
    
