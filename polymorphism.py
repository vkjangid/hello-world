class Father:
    __car = 'range rover evoque'
    __bank_balance='$ 4000 billion'
    __house='mansion'
    def business(self):
        print('airline business')
    def to_marry(self):
        print('preeti')

# here __ will make any variable or function private
# it is called encapsulation

class Son(Father):
    def to_marry(self):
        print('gf')

print(Son.car)
print(Son.bank_balance)
print(Son.house)

# after using __ in the parent class now it will throw an error because now Son can't access car/house/bank_balance

obj=Father()
obj.to_marry()
obj1 = Son()
obj1.business()
obj1.to_marry()