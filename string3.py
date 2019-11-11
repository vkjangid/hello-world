'''s='hi python'
i=0
while i<len(s):
    print(s[i])
    i+=1'''

'''s='hi python'
i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1

    or

s[::-1]'''

'''a=input('enter some string')
for i in range(len(a)):
    for j in range(3):
        print(a[i],end='')'''


a="vivek"
b=12345
for i in range(3):
    c=input("enter the useraname")
    d=input("enter the password")
    if c==a and d==b:
        print("login is successful")
	break
    else:
        print("username or password is incorrect")
    if i>1:
        print("your account has been blocked,please contact to the bank")


    
