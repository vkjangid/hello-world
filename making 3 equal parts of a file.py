with open('c://users/vivek/Desktop/python/test2.txt','r') as read:
    a=read.readlines()
    b=int(len(a)/3)
    c=[]
    d=[]
    e=[]
    for i in range(0,b):
        c.append(a[i])
    for i in range(b,b+b):
        d.append(a[i])
    for i in range(b+b,len(a)):
        e.append(a[i])

with open('c://users/vivek/Desktop/python/part1.txt','w') as write:
    write.writelines(c)

with open('c://users/vivek/Desktop/python/part2.txt','w') as write:
    write.writelines(d)

with open('c://users/vivek/Desktop/python/part3.txt','w') as write:
    write.writelines(e)

