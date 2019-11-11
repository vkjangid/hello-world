a=input('enter some string')
if len(a)==1:
    pass
elif len(a)==2:
    print(a*2)
elif len(a)==3:
    print(a+a[-1])
else:
    print(a[:2]+a[len(a)-2]+a[len(a)-1])
    
    
