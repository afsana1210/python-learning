t=(1,2,3)
print t[0]
from collections import namedtuple
Dog=namedtuple('Dog','age breed name')
sam=Dog(age=2,breed='Lab',name='sammy')
print sam
print sam.age
print sam[0]