#deleting the given specific line

'''d=int(input('enter any number'))
with open('C:/users/vivek/Desktop/python/test1.txt','r') as a:
    c=a.readlines()
    print(c)
    del(c[d-1])
with open('C:/users/vivek/Desktop/python/test1.txt','w') as b:
    print(c)
    b.writelines(c)'''
        



#deleting the range of lines by given two numbers

'''try:
    with open('C:/users/vivek/Desktop/python/test1.txt','r') as read:
        c=read.readlines()
        print(c)
        a=int(input('enter the number of starting line'))
        b=int(input('enter the number of last line'))
        count=0
        for i in range(a,b+1):
            del(c[i-1-count])
            count+=1
    with open(r'C:/users/vivek/Desktop/python/test1.txt','w') as write:
        print(c)
        write.writelines(c)
except IndexError as e:
    print(e)'''
