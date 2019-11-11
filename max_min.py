'''a=input('enter any number')
a=int(a)
b=input('enter any number')
b=int(b)
c=input('enter any number')
c=int(c)
d=input('enter any number')
d=int(d)
print(max(a,b,c,d))
print(min(a,b,c,d))'''


l=[0,0,0,0]
for i in range(4):
    l[i]=input('enter a number')
print(max(l))
print(min(l))
