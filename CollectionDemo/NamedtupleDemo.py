#Named tuple same as tuple but use name rather than index

from collections import namedtuple
Emp=namedtuple('Emp','id name salary')
e=Emp(id=101,name='Riya',salary=20000)

#accessing the values
print(e)

#Individual by index
print(e[2])

#by attribute
print(e.name)

#Methods
print(e.count(101))
print(e.index(101))
