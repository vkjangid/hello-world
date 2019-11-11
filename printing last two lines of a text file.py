try:
    def last_two_values():
        with open(o,'r') as read:
            a=read.readlines()
            print(a)
            for i in range(2,0,-1):
                print(a[-i])
    o='c://users/vivek/Desktop/python/test2.txt'
    last_two_values()
        
except FileNotFoundError:
    import random
    with open(o,'w') as write:
        for i in range(10):
            n=random.randrange(100,50000)
            n=str(n)
            write.write(n+'\n')
    last_two_values()
