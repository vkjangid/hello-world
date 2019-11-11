def change(a,b):
    c=a.upper()
    d=b.upper()
    j=0
    l=[]
    for i in range(len(c)):
        if c[i]==' ' or c[i]==',':
            if c[j:i]==d:
                l.append(c[j:i])
            else:
                l.append(a[j:i])
            j=i+1
        if i==len(c)-1:
            if c[j:i+1]==d:
                l.append(c[j:i+1])
            else:
                l.append(a[j:i+1])
    print(l)
    for i in range(len(l)):
        if l[i]==d:
            l[i]=r
    print(" ".join(l))
    
a=input('enter any sentence')
b=input('enter the word you wanna replace')
r=input('replacement word')
change(a,b)
