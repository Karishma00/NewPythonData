
#Exercise 18 pick even in function with args
def myfunc(*args):
    a = []
    for i in args:
        if i%2==0:

            a.append(i)
    return a

print(myfunc(10,20,30,7))