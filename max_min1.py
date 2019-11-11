l=[0,0,0,0,0]
for i in range(5):
    l[i]=int(input('enter a number'))
maximum=l[0]
minimum=l[0]
for i in l:
    if maximum>i:
        continue
    else:
        maximum=i
for i in l:        
    if minimum<i:
        continue
    else:
        minimum=i
print('maximum value is=',maximum)
print('minimum value is=',minimum)
    




    

