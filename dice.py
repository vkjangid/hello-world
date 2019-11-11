import random
d=0
for i in range(1,11):
    print(i,'chance--')
    a=random.randrange(1,6)
    b=random.randrange(1,6)
    print('1st dice value=',a,'    ','2nd dice value=',b)
    c=a+b
    print('total dice value=',c)
    if(d+c)>50:
        if(i>9):
            print('you lose the game')
        continue
    else:
        d=d+c
        print('total chance values=',d)
    if d==50:
        print()
        print('you won the game')
        break
    print()
    
