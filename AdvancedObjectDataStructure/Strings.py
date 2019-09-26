#Strings

str1="Advanced Strings"


print('Capitalize : ',str1.capitalize())
print('Title :',str1.title())
print('Count :',str1.count('a'))
print('Find : ',str1.find('s'))
print('Center :',str1.center(20,'.'))#Places the string between . and length is 20

s2='Expanding\tStrings'
print('Expand Tabs :',s2.expandtabs())

#Alphanumeric
n='12333'
print(f'{n} is : alphanumeric {n.isalnum()}')

#Alphabatic
print(f'{n} is : alphbatic {n.isalpha()}')

#endswith
a='Abcde'
print(f'{a} is end with e : {a.endswith("e")}')

#Built in RegExpresssion
#split
x='Spliting the string'
print(f'X : {x} after spliting by i :{x.split("i")}')

#partiotion
print(f'X : {x} after Partition by i :{x.partition("i")}')

