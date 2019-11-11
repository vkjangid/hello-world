#we have to compare two lists, if any value of second list is present in the first list 
#then that value will be converted into 0
#and after that we have to add the vaues of second list

def verification():
    for i in range(len(l1)):
        for j in l:
            if l1[i]==j:
                l1[i]=0
    
def output():
        print(l1[0]+l1[1]+l1[2])

a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
l=[2,6,4,7,9]
l1=[a,b,c]
verification()
output()
