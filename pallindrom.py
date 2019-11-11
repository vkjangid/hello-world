a=input('enter any number')         
a=list(a)
b=list(a)
c=len(a)-1
for i in range(len(a)):
    b[i]=a[c]
    c-=1
if a==b:
    print('the given value is a pallindrom value')
else:
    print('the value given is not pallindrom value')


