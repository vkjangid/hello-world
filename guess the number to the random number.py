import random
a=random.randrange(100,1000)
a=str(a)
for l in range(10):
    b=input('guess the number of 3 digits')
    b=str(b)
    t=0
    i=0
    p=0
    for j in range(3):
        count=a.count(b[i])
        if count==0:
            if i==2:
                print(b[i],'not present in the number')
                break
            print(b[i],'not present in the number')
            i+=1
            continue
        else:
            for p in range(p,3):
                if b[i]==a[p]:
                    if i==p:
                        t+=1
                        print(b[i],'is present at the right place')
                        i+=1
                        p+=1
                        break
                    else:
                        print(b[i],'is present in the number but not in the right place')
                        i+=1
                        break        
    if t==3:
        print('you guessed the number correctly')
        break           
    
