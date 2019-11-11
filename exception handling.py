'''try:
    s='hi pyhton'
    s.index('hello')
    print(s)
except Exception:
    print('hello not found')
print('end')


try:
    s='hi pyhton'
    s.index('hello')
    print(s)
except Exception as e:
    print(e)
print('end')'''
#here e is the message when an error comes

'''try:
    a=20
    b=30
    a=b
    b=0
    res=a/b
    print(res)
except ZeroDivisionError as ex:
    print(ex)
print('end')'''
#here it will just handle the error of zero division
#other errors will not be handled in this case

'''try:
    a=cd
    a=20
    b=30
    a=b
    b=0
    res=a/b
    print(res)
except ZeroDivisionError as ex:
    print(ex)
print('end')'''

'''try:
    a=cd
    a=20
    b=30
    a=b
    b=0
    res=a/b
    print(res)
except NameError as ex:
    print(ex)
except ZeroDivisionError as ex:
    print(ex)
print('end')'''
#we can use multiple except with single try

'''try:
    1/0
except ZeroDivisionError as ex:
    print('inside zero division')
except Exception as ex:
    print('inside exception')'''

'''try:
    a=20
    b=30
    print(a)
    print(b)
    try:
        a=80
        a/0
    except ValueError:
        print('value error')
except Exception:
    print('exception')
print('end')'''
#this is an example of nested exception handling





