print('length of password should be greater than 6\n''there should be atleast one capital letter, one numeric value and one special character which should be @ or # or $')
a=input('enter the password')
p=bool()
q=bool()
r=bool()
j=0
for i in range(1):
    if len(a)<6:
        print('length of password is less than 6')
        break
    while p==False:
        if a[j].isupper():
            p=True
        elif j>=len(a)-1:
            print('there is no capital letter in the password')
            break
        j+=1
    j=0
    while q==False:
        if a[j].isdigit():
            q=True
        elif j>=len(a)-1:
            print('there is no digit in the password')
            break
        j+=1
    j=0
    while r==False:
        if a[j]=='@' or a[j]=='#' or a[j]=='$':
            r=True
        elif j>=len(a)-1:
            print('there is no specified special character in the password')
            break
        j+=1
if p==q==r==True:
    print('password is correct')
    
