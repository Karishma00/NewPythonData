

#Using map even or odd

def check(s):
     if len(s)%2==0:
         return 'Even '
     else:
         return 'Odd'

n=['abces','afd','hg']
for i in map(check,n):
      print(i)



