#Generate the fibbonacci series


def fib(n):
    a=1
    b=1
    for i in range(n):
        yield  a
        a,b=b,a+b

print('The Fibbonacci series is :')
for i in fib(20):
    print(i)
