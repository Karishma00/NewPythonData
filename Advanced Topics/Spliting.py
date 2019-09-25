#Split the string by term and ,

import re
s= 'Hello, Your email is abc@gmail.com ??'
spl='@'

print('The String is  : ',s)
print('The splited string : ',re.split(spl,s))

#normal split
print('Normal Split : ',s.split())


