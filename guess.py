a=5
for i in range(3): 
    b=input('guess the number=')
    b=int(b)
    if b!=a:
        if i>1:
            print('game over')
            break
        else:
            print('your guess is wrong')
    else:
        print('your guess is right')
        break
    
