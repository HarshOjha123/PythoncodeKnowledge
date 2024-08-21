c=float(input("Enter the DEcimal value"))
d=str(c)
add=0
for x in d:
    if x==".":
        continue
    add=add+int(x)
print(add)