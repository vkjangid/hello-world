a=0
b=1
c=0
d=int(input('enter a value'))
for i in range(d):
   c=a+b
   if c>=d:
      break
   print(c)
   a,b=b,c
