#converting list to dictionary

l=['ram-20','shyam-30','mona-40']
d={}
a=''
b=''
for i in l:
    for j in range(len(i)):
        if i[j].isalpha():
            a=a+i[j]
        if i[j].isdigit():
            b=b+i[j]
    d.update({a:b})
    a=''
    b=''
print(d)


#changing dictionary values

'''d={'ram':40,'shyam':40,'mohan':20,'rohit':60,'mohit':90}
d1={}
for i in d:
    if d[i]==40:
        d1.update({'vivek':40})
    elif i[0]=='m':
        d1.update({i:40})
    else:
        d1.update({i:d[i]})
print(d1)'''
        
        
