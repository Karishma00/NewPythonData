#exercise 19 skyline

def myfun(s):
    x=[]
    new = ""
    for i,a in enumerate(s):
        if i%2==0:
            a=a.upper()
            x.append(a)
        else:
            x.append(a)

    for d in x:
        new += d

    return new

print(myfun('abcde'))


