#Python debugger

import pdb
a=[1,2,3,4,5]
b=10
c=4

res=b+c
print(res)

pdb.set_trace()

res1=a+c
print(res1)
