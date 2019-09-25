#Rgular expression search in string

import re
s ='This is the string with Hello not Hii'
p =['Hello','Hi']

for i in p:
    print('Serching for "%s" in \n "%s"' %(i,s))
    if re.search(i,s):
        print('\n Match found !! \n ')
    else:
        print('\n Match not found !!\n ')

match=re.search(p[0],s)
print(type(match))
print(match.start())
print(match.end())




