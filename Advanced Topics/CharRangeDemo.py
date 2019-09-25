#Character between the given range

import re

def find_multi_pattern_char(patterns,strings):
    for p in patterns:
          print('Searching in the string %r'%p)
          print(re.findall(p,strings))
          print('\n')


str1='This is the Character Range Demo Example '
t=['[a-z]+','[A-Z]+','[a-zA-Z]+','[A-Z][a-z]+']

#pattern sequences are 1.set of lower case 2.set of upper case 3.set of lower case and upper case 4.One upper case followed by lower case
find_multi_pattern_char(t,str1)