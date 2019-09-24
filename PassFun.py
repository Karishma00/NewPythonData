#Passing the function and calling by that

def hello():
    print('Hello ..')

def other(a):
    print('Other fun()')
    print(a())


print('Call to the hello')
hello()

print('Call to the Other')
other(hello)#By as a variable