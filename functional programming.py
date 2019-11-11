'''add=lambda a:a+20
print(add(20))'''

#here a lambda function is a one line function
#after a lambda we will give arguments
#and after that we will define the working of this function

'''square=lambda a:a*a
print(square(4))'''


'''def fun(a):
    return lambda b:b*a
lam=fun(20)
print(lam(30))'''

#we can define lambda function in the normal functions
#it will be like function in the function

'''lam=lambda a,b:lambda x:lambda y:a*b*x*y
print(lam(2,2)(2)(2))'''

# or

'''lam=lambda a,b:lambda x:lambda y:a*b*x*y
var=lam(2,3)
var1=var(2)
print(var1(2))'''

#this is a example of nested lambda function

'''a=int(input('enter any number'))
lam=lambda a:'yes' if a>4 else 'no'
print(lam(a))'''

#we are using if else in the lambda function

'''def square(a):
    for i in range(len(a)):
        a[i]=a[i]**2

l=[2,4,5]
square(l)
print(l)'''

#this is a program where it will square all the values of the list

'''l=[2,4,5]
print(list(map(lambda a:a**2,l)))'''

# this is a same program as above but it is using map with lambda function for code optimisation

'''l=[2,4,5]
def sq(x):
    return x*x
print(list(map(sq,l)))'''

#in the map function we can also use user defined function, this is a same program as above 

'''l=[]
l1=[2,4,5]
l2=[4,16,25]
def multiply(a,b):
    for i in range(len(a)):
        l.append(a[i]*b[i])
    print(l)
multiply(l1,l2)'''

#this is a program where it will multiply all the values of two list with each other

'''l1=[2,4,5]
l2=[4,16,25]
print(list(map(lambda a,b:a*b,l1,l2)))'''

#this is a program as same as above but it is using map with lambda function

'''l=[1,8,6,7,2,5,4,3]
def fil(a):
    l1=[]
    for i in range(len(a)):
        if a[i]>4:
            l1.append(a[i])
    print(l1)
fil(l)'''

#this is a program where it will add all the values in the new list if the value is greater than 4

'''l=[1,8,6,7,2,5,4,3]
print(list(filter(lambda a: a>4 ,l)))'''

#this is a same program with the use of filter and lambda function
#filter will work like if the condition is true then it will save the value in its object otherwise it will just neglect the value

'''l=[1,2,3,4]
def mul(l):
    res=1
    for i in range(len(l)):
        res=res*l[i]
    return res
print(mul(l))'''

#this is a program where we have to multiply every elements of the list to each other

'''from functools import reduce 
l=[1,2,3,4]
print(reduce(lambda a,b:a*b,l))'''

#this is a same program as above but here we are just using reduce and lambda functions

'''l=iter([1,2,3,4,5])
print(type(l))
for i in l:
    print(i)
for j in l:
    print(j)'''

#iter object is a value where it will read one elements only once

'''l=iter([1,2,3,4,5])
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())
print(l.__next__())'''

#l.__next__() is a inbuilt function of the iter object where it will read its elements one by one

'''l=iter([1,2,3,4,5])
a=0
while a<5:
    print(l.__next__())
    #print(next(l))
    a+=1'''

#we can use a sdf next(l) it will also read the elements of the object one by one

'''def sum(a,b):
    res1=a+b
    return res1
    res2=a*b
    return res2
print(sum(4,2))'''

#because here 2nd return wiil not work,when the compiler will see the first return it will go back to the calling function
#and the code written under the first return will not be excuted

'''def sum(a,b):
    res1=a+b
    yield res1
    res2=a*b
    yield res2
    res3=a/b
    yield res3
gen=sum(4,2)
print(next(gen))
print(next(gen))
print(next(gen))'''

#so yield can work here if we want to return multiple values
