#Returns all the matches

import re
s ='This is the example of findall and This is performed by findall'

f='This'

print('String : ',s)
print('Pattern :',f)

print('Matches : ',re.findall(f,s))






