def validation(a):
    try:
        a=input('enter the age')
        a=int(a)
        return a
    except ValueError:
        print('your given input is string')
        return a
def age(a):
    if a<=0:
        try:
            raise ValueError('your given age is either zero or below zero')
        except ValueError as e:
            print(e)
    if 0<a<18:
        try:
            raise ValueError('age is below 18, not eligible for voting')
        except ValueError as e:
            print(e)
    if a>=18:
        print('you are eligible for voting')

a=''
while type(a)==str:
    a=validation(a)
age(a)


'''try:
    a=20
    if a==20:
        raise ValueError(20)
except Exception as ex:
    print(ex)'''
