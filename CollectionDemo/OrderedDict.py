
from collections import OrderedDict
#Normal dictionary in not oredered

d = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
for i,j in d.items():
    print(i,' ',j)
d = OrderedDict()
for i1,j1 in d.items():
    print(i1,' : ',j1)






