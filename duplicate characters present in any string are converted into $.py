a="xyzaaxyf"
a=list(a)
print(a)
b=1
for i in range(len(a)):
    for j in range(b,len(a)):
        if a[i]==a[j]:
            a[j]='$'
    b+=1
print("".join(a))    

