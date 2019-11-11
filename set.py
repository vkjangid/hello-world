s=set()
#defining empty set

s={'a','b','c'}
#defining set with values

s.add('value')
#adding some value in the set

s.remove('value')
#removing some value in the set
#but here if the value given is not present in the set then it will show error

s.discard('value')
#discard also remove value in the set
#but here if the value given is not present in the set then it will not show error


odd={1,3,5,7}
even={2,4,6,8}
odd.union(even)
#it will combine the values of odd and even sets

odd={1,3,5,7}
prime={2,3,5,7}
odd.intersection(prime)
#it will take common values present in both sets

s1={'a','b','c','d'}
s2={'c','a'}
s1.issubset(s2)
#it will check that is s1 is a part of s2 and output will be given in true or false

s1.issuperset(s2)
#

s1.difference(s2)
#the values will be removed from s1 which is present in s2
