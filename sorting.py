l=[9,6,7,3,8]
for i in range(5):
    for j in range(4):
        if l[j]<l[j+1]:
            continue
        else:
            l[j],l[j+1]=l[j+1],l[j]    
print(l)


l=[9,6,7,3,8]
for i in range(5):
    for j in range(4):
        if l[j]>l[j+1]:
            continue
        else:
            l[j],l[j+1]=l[j+1],l[j]    
print(l)

'''import random
l=[0,0,0,0,0]
for i in range(5):
    l[i]=random.randrange(1,20)
print(l)    
a=1
for i in range(5):
    for j in range(a,5):
        if l[i]<l[j]:
            continue
        else:
            l[i],l[j]=l[j],l[i]
    a+=1        
print(l)

