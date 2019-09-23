#filters the i/p based on function


def odd(n):
    if n%2!=0:
        return n

l=[1,4,9,7,8,10]
for i in filter(odd,l):
    print(i)