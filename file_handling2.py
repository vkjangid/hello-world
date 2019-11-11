r'''a=open(r'C:\Users\vivek\Desktop\python\test1.txt','w')
a.write('vk')
a.close()'''

#write operation will remove all the data present in the file and add the data we want to write
#if the file does not present at the given address then it will create for us
#we have to close the file after writing data

'''data=['btm\n','jpnagar\n','jayanagar']
a.writelines(data)
a.close()'''

r'''a=open(r'C:\Users\vivek\Desktop\python\test1.txt','a')
data=['\nhi\n','hello\n','hey\n']
a.writelines(data)
a.close()'''

#append function is just as same as the write function but the difference is just that it will keep the data present in the file if the data is present


with open(r'C:\Users\vivek\Desktop\python\test1.txt','w') as f:
    f.write('hi')
    print(f.closed)
print(f.mode)
print(f.closed)

#with used for automatically close the file after the write block execution is completed
#mode function will give us operation detail which was performed in the file
#closed function will give us the detail that the file is closed or not


#for using the read and write operation we can use r+
