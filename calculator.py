def add(a,b):
    print('addition',a+b)

def sub(a,b):
    print('subtraction',a-b)

def mul(a,b):
    print('multiplication',a*b)

def div(a,b):
    print('division',a/b)

print('1 for add       2 for subtraction      3 for multiply      4 for division')
o=int(input('choose the operation'))
a=int(input('enter first value'))
b=int(input('enter second value'))
if o==1:
    add(a,b)
elif o==2:
    sub(a,b)
elif o==3:
    mul(a,b)
else:
    div(a,b)
