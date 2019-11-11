o='c://users/vivek/Desktop/python/error.txt'

def making_list(b):
    l=[]
    p=0
    present=bool()
    for i in range(len(b)):
        if b[i]==' ':
            l.append(b[p:i])
            p=i+1
        if i==len(b)-1:
            l.append(b[p:i])
    for i in l:
        i=i.upper()
        if i=='ERROR' or i=='EXCEPTION':
            present=True
            print(i,'is present in the line',count)
    if count==len(a)-1:
        if present==False:
            print('error and exception words are not present in the file')
    
with open(o,'r') as read:
    a=read.readlines()
    count=1
    for i in range(len(a)):
        making_list(a[i])
        count+=1
    
