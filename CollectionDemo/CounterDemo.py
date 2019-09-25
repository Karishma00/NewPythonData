#Count in the list

from collections import Counter
list1=[1,2,8,3,4,5,3,6,7,6,2,3,4,1,9,7,5,6]

#count the occurences of number in list

print('List :',Counter(list1))

s='Advanced Topics Python'
print('Counting chracters ',Counter(s))

words='How many time show up this how many count . .'
w=words.split()
print('Word Count',Counter(w))

#commin word
x=Counter(w)
x.most_common()
print(x)

#count the values
print(sum(x.values()))

