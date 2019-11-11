'''l=[4,1,2,3,4,5,2,1,2,3,6]
l1=[2,3,4]'''

l=[]
for i in range(5):
    l.append(int(input('enter some value')))
print(l)
l1=[]
for i in range(3):
    l1.append(int(input('enter some value')))
print(l1)
i=0
for j in range(len(l)):
    if l[j]==l1[i]:
        i+=1
        if i>=len(l1):
            print('series of ',end='')
            for i in range(len(l1)):
                print(l1[i],' ',end='')
            print('is present',end='')
            break
        continue
    if j>=len(l)-1:
        print('series of ',end='')
        for i in range(len(l1)):
            print(l1[i],' ',end='')
        print('is not present',end='')
    i=0
