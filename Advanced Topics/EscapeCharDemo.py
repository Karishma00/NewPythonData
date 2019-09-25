#Escape characters
import  re

def find_multi(patterns,strings):
    for p in patterns:
          print('Searching in the string %r'%p)
          print(re.findall(p,strings))
          print('\n')


str1='This is the 01 Escape Character  9 Example # '
t=[r'\d+',r'\D+',r'\s+',r'\S+',r'\w+',r'\W+']

print(find_multi(t,str1))

