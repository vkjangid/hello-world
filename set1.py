# removing duplicate values from list and printing in descending order

'''l=[1,5,6,2,1,3,8]
l=set(l)
l=list(l)
for i in range(len(l)):
    for j in range(len(l)-1):
        if l[j]>l[j+1]:
            continue
        else:
            l[j],l[j+1]=l[j+1],l[j]  
print(l)'''


# printing common values present in two lists

'''l1=[1,3,4,6,8]
l2=[1,4,9,10]
l1=set(l1)
l2=set(l2)
l3=l1.intersection(l2)
l3=list(l3)
print(l3)'''


# taking input as a set and find that new given input is present in the first set

'''s=set()
for i in range(5):
    s.add(int(input('enter some value')))
print(s)

a=set()
a.add(int(input('enter a value')))

if a.issubset(s):
    print('it is present')
else:
    print('value does not exist')'''


# showing the index of the values where the addtion of two index values is equal to the user given input

l=[30,20,30,10,40,50]
a=int(input('enter any number'))
b=1
for i in range(len(l)):
    for j in range(b,len(l)):
        if a==l[i]+l[j]:
            print(i,j)
    b+=1
        