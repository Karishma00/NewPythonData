#exercise 19 skyline

def myfun(s):
    x=[]
    for i,a in enumerate(s):
        if i%2==0:
            a=a.upper()
            x.append(a)
        else:
            x.append(a)
    return x

print(myfun('abcde'))


