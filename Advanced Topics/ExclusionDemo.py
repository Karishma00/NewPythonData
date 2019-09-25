#Excluding the content

import re
st='This is the String !!, That Containing the ?? and ... etc'
a='[^!.? ]+'

#Exclusion is find the !.? is removed from the String
print('String :',st)
print('Excluded string :',re.findall(a,st))
