'''try:
    1/0
except Exception as ex:
    print(ex)
finally:
    print('inside finally')'''

#finally block will execute everytime the code will run

'''try:
    a=20
except Exception as ex:
    print(ex)
else:
    print('ex')'''

#else code will only run if the code does not have an exception
#if any exception come then else code will not run

'''try:
    a=20
    exit(1)
except Exception as ex:
    print(ex)
else:
    print('ex')'''

#exit() function used to kill the program right away when compiler compile the exit line

'''a='hi {},hello {}'
a=a.format('python','java')
print(a)'''

#format function can add the values at the braces define in the string

'''a='hi {1},hello {0}'
a=a.format('python','java')
print(a)'''

#we can use key in the braces

'''a='hi {j},hello {p}'
a=a.format(p='python',j='java')
print(a)'''

#we can use variables in the braces

'''try:
    1/0
finally:
    print('hi')'''

#try can be used either with the except or with finally

'''try:
    1/0
except Exception:
    print('exception')
else:
    print('else')
finally:
    print('hi')'''

#after try block there has to be an except block and after that we can use else block
#and finally block can be used after the try and exception block

try:
    a=20
    print(a)
    try:
        n='hi'
        try:
            print(n)
            n.index('z')
        finally:
            print('end')
    except AttributeError:
        print('inside attribute error')
except ValueError as ex:
    print(ex)
except Exception:
    print(ex)
else:
    print('else')
finally:
    print('end')

    
        
