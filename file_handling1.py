a=open(r'C:\Users\vivek\Desktop\python\test.txt','r')
b=int(input('enter the line number'))
c=a.readlines()
if b<=len(c):
    print(c[b-1])
else:
    print('line is not present')



