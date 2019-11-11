a=open(r'C:\Users\vivek\Desktop\python\test.txt','r')
print(a)

'''b=a.read()
print(type(b))'''

#read function will take all the data present in the file and put it in as a string in the variable

b=a.readline()
print(b)
print(type(b))
b=a.readline()
print(b)
print(type(b))
b=a.readline()
print(b)
print(type(b))
b=a.readline()
print(b)
print(type(b))

#readline() function will take the data of the single line and put it as a string in the variable

b=a.readlines()
print(b)
print(type(b))

#readlines() function will take all the data and put it in the list

