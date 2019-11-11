'''l=['a','b','c','d','e']
a=1
for i in l:
    for j in l:
        print(i)
    if a!=len(l):
        print('-------------------')    
    a+=1

l=['a','b','c','d','e']
a=1
for i in l:
    for j in l:
        print(j)
    if a!=len(l):
        print('-------------------')    
    a+=1'''

'''l=input('enter')
l=list(l)
print(l)
print(type(l))'''

'''l=[1,2,3,4]
for i in l:
    if i==4:
        pass
    print(i)
else:
    print('hi')'''

#if we use else with for then it will work until and unless the for statement does not break

'''l=['line1','fine2','error','exception','success','line5','failure']
count=0
for i in l:
    if i=='failure' or i=='exception' or i=='success':
        print(i,count)
    count+=1'''


l=['a','b','c']
for i,j in enumerate(l):
    print(i,j)

#enumerate is a inbuilt function who gives the value with index of the value    



