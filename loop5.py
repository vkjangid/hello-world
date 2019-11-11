num=input('enter any number=')
num=int(num)
if num%2==0:
    num1=(num/2)+1
    num1=int(num1)
    num2=0
    for a in range(0,num1):
        if a==0:
           print('*')
           continue
        else:   
           for b in range(num2+2):
              print('*',end='')
        num2+=2 
        print('')
    num3=num1+1
    for a in range(num3,num+2):
        if a==num+2-1:
           print('*')
           break
        for b in range(num2-2):
            print('*',end='')
        print('')
        num2-=2
else:
    num1=(num/2)+1
    num1=int(num1)
    for a in range(1,num1+1):
        for b in range((a*2)-1):
           print('*',end='')
        print('')
    p=num-2    
    for a in range(num,num1,-1):
        for b in range(p):
            print('*',end='')
        print('')
        p=p-2
