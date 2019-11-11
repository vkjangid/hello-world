#common values between two dictionaries

'''d1={'key1':40,'key2':30,'key3':40,'key4':90,'key5':60}
d2={'key1':20,'key2':30,'key3':30,'key4':80,'key5':60}
d3={}
for i in d1:
    if d1[i]==d2[i]:
        d3.update({i:d1[i]})
print(d3)'''



#adding the value of common keys

'''d1={'key1':40,'key2':30,'key3':40,'key4':90,'key5':60}
d2={'key1':20,'key6':30,'key7':30,'key4':80,'key5':60}
d3={}
for i in d1:
    for j in d2:
        if i==j:
            d3.update({i:d1[i]+d2[j]})
print(d3)'''



#print highest key value

'''d={'ram':97,'shyam':80,'mohit':60,'sohan':95}
m=max(d.values())
n=''
for i in d:
    if m==d[i]:
        n=i
print(n+' has highest marks, which is ',m)'''



#adding the marks of same student and calculating average of the marks

l=[{'name':'ram','subject':'maths','marks':80,'year':2018},{'name':'ram','subject':'maths','marks':75,'year':2019}]
d1={}
years=[]
total=0
for i in l:
    for j in i:
        if j=='year':
            years.append(i.get(j))
        elif  j=='marks':
            total+=i.get(j)
for i in l[0]:
    if i=='name':
        d1.update({i:'ram'})
    if i=='subject':
        d1.update({i:'maths'})
    if i=='marks':
        d1.update({'marks':total})
        d1.update({'avg':total/len(l)})
    if i=='year':
        d1.update({'year':years})
print(d1)
