'''t=(1,2,3,4)
print(type(t))
for i in t:
    print(i)'''

'''t[2]

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)'''

#tuple does not support any types of modification,once it is declared then we can't modify the data

'''t=(1,2,3,4)
t=list(t)
for i in range(2):
    del t[len(t)-1]
t=tuple(t)
print(t)
print(type(t))'''

'''l1=[1,2,3,4]
t1=(1,2,3,4)
len(l1)
len(t1)
l1.append(6)
print(l1)
t1.append(8)
print(t1)'''

#there is no append function in tuple because we are trying to modify the tuple and tuple does not support any modification

'''l1.extend([4,5])
print(l1)

t1.extend([4,5])
print(t1)'''

#extend will work with only list not with extend

'''l=[1,2,3,4]
print(l.index(2))
print(l.index(4,0,len(l)))

t=[1,2,3,4]
print(t.index(4,0,len(t)))'''

#index function is used for printing index of any value

'''print('max=',max(l))
print('min=',min(l))
print('max=',max(t))
print('min=',min(t))

print(l.pop(3))
print(l)'''

#pop function is used for deleting the value of the given index, but tuple does not suppport this function

'''l=[1,2,3,4]
l.remove(3)
print(l)

l.remove(5)'''

#remove function is used for deleting the value in the list
#difference between remove and pop is that pop use index value and remove function use value in the bracket

'''l[2]=6
print(l)'''

'''l=[1,2,3,4]
l.insert(3,[1,2,3])
print(l)'''

'''l=[1,2,8,4,5]
l.reverse()
print(l)'''

#reverse is used for changing the value in the opposite form

'''l.sort()
print(l)

l.sort(reverse=True)
print(l)'''

#sort is used for sorting the values in ascending or descending order

'''l=[1,2,2,4,5,5]
l=set(l)
print(l)
print(type(l))

t=[1,2,2,4,5,5]
t=set(t)
print(t)'''

#set is a data type here

'''l=[1,2,3,4]
l.clear()
print(l)'''

#clear is user for deleting all the values in the list

'''l=[1,2,3,4]
t=[1,2,3,4]
l2=l
print(l)
print(l2)
del l2[2]
print(l)
print(l2)'''


l=[1,2,3,4]
t=[1,2,3,4]
l2=l.copy()
print(l)
print(l2)
del l2[2]
print(l)
print(l2)

#if we use = operator then l2 is gonna point to the values of the l so if we delete any values in l2 then it will delete the value of l
