a=int(input('enter the first line number'))
b=int(input('enter the last line number'))
c=open('c://users/vivek/Desktop/python/test.txt','r')
d=c.readlines()
for i in range(a,b+1):
    try:
        print(d[i-1])
    except IndexError:
        print(i,'is out of range')
