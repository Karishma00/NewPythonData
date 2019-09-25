#repetition Syntex example
import re


def find_multi_pattern(patterns,strings):
    for p in patterns:
          print('Searching in the string %r'%p)
          print(re.findall(p,strings))
          print('\n')


str1='aaaabbbaa..ababa..aabbbbb.babaa..aaabbb'
t=['ab*','ab+','ab?','ab{2}','ab{2,5}']

find_multi_pattern(t,str1)


