'''def test():
    print('inside test')


def fun():
    for i in range(5):
        print(i)
        test()


fun()
print(2+4)
while True:
    print('hello world')
    break'''

'''for i in range(2):
    for j in range(2):
        while True:
            for k in range(2):
                if k == 1:
                    break
            break
'''

import os
print(os.getcwd())  # it will print the current directory where the file is present
os.chdir('C:/users')    # it will change the directory
print(os.getcwd())
print(dir(os))