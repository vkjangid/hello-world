import random
a=input('enter 1st four digit number')
a=int(a)
b=input('enter 2nd four digit number')
b=int(b)
if (a>=1000 and a<=9999) and (b>=1000 and b<=9999):
    if(a>b):
        a,b=b,a
    print('the generated otp is ',random.randrange(a,b))
else:
    print('entered number is wrong')
