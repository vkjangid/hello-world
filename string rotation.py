#full rotation

'''a=input('enter some string')
b=int(len(a)/2)
print(a[b::]+a[:b:])'''


#left or right rotation

a=input('enter some string')
b=input('enter type of rotation')
c=int(input('enter the index where the rotation will be done'))
if b=='right':
    print(a[c::]+a[:c:])
else:
    print(a[-c::]+a[-len(a):-c:])

