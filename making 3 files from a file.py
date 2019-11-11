def duplicates(a):
    l=[]
    for i in range(len(a)):
        count=a.count(a[i])
        if count>1:
            count1=l.count(a[i])
            if count1==0:
                l.append(a[i])
    with open('c:/users/vivek/Desktop/python/duplicate_data.txt','a') as write:
        write.writelines(l)

def unique(a):
    for i in range(len(a)):
        count=a.count(a[i])
        if count==1:
            with open('c:/users/vivek/Desktop/python/unique_data.txt','a') as write:
                write.write(a[i])

def no_duplicates(a):
    l=[]
    for i in range(len(a)):
        count=l.count(a[i])
        if count==0:
            l.append(a[i])
    with open('c:/users/vivek/Desktop/python/no_duplicates.txt','a') as write:
        write.writelines(l)

with open('c:/users/vivek/Desktop/python/test3.txt','r') as read:
    a=read.readlines()
print(a)
duplicates(a)
unique(a)
no_duplicates(a)
