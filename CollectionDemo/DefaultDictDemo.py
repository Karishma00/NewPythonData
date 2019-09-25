#same as dict but provide the default vlue for key

from collections import defaultdict

dict1={'a':1,'b':2,'c':3}
print(dict1)

#give the default dict
dict1=defaultdict(lambda :2*2)
print(dict1['d'])#Otherwise Key error occurs that not occurs by defaultdict


print(dict1)