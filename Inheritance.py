class Father:
    car = 'lykan hypersport'
    bank_balance = '$ 4000 billion'
    house = 'mansion'

    def business(self):
        print('airline business')


'''print(Father.car)
print(Father.bank_balance)
print(Father.house)
obj = Father()
obj.business()'''


class Son(Father):
    pass


print(Son.car)
print(Son.bank_balance)
print(Son.house)
obj1 = Son()
obj1.business()

# we can inherit multiple classes to a single class