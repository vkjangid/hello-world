#this is how we define a function

'''def add(num1,num2):
	return(num1+num2)

#return will just give the output of the statement to the calling function
    
print(add(2,3))         or          add(2,3)'''

#this is how we can call a function

def add(a,b):
    print(a)
    print(b)
    print(a+b)
    return a,b,4

print('start')
z=add(2,5)
print(z)

# taking two input first name and last name and printing full name with the help of funtion 

'''def name(a,b):
    return a+' '+b

a=input('enter first name')
b=input('enter last name')
print(name(a,b))'''

'''types of arguments-

    1. required positional arguments
    2. required non positional arguments
    3. default arguments
    4. var arguments'''

#required positional arguments

'''def add(a,b,c):
    print(a)
    print(b)
    print(c)

print(add(1,2,4))

#required non postitional arguments

def add(a,b,c):
    print(a)
    print(b)
    print(c)

print(add(b=4,a=1,c=2))

#default arguments

def add(a,b,c,d=5):
    print(a)
    print(b)
    print(c)

print(add(1,4,2))

# var args

def add(a,b,*c):
    print(a)
    print(b)
    print(c)

print(add(1,2,4,6,3,7))'''

#in default and var args, defining any value in function and putting * in any function it should be at last

'''def case(a):
    if a.isupper():
        print(a.lower())
    if a.islower():
        print(a.upper())
a=input('enter any name')
case(a)'''

def case(a):
    for i in range(len(a)):
        if a[i].isupper():
            return a.lower()
    else:
        if a.islower():
            return a.upper()
a=input('enter any name')
case(a)