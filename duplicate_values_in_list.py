'''l=[5,5,3,7,7,5,5,7,2,2,3]
l1=[]
for i in l:
    ct=l.count(i)
    if ct >1:
        if i not in l1:
            l1.append(i)
            #print(i,"counts is ",ct)
    else:
        l1.append(i)
print(l1)'''


l=[5,5,3,7,7,5,5,7,2,2,3]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
    else:
        l1.append(i)
print(l1)