l=[0,0,0,1,1,2,2,3,4,4,4,5]
count=-1
for x in l:
    for y in l:
        if x==y:
            count+=1
    print(x," ",count)            