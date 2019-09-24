#Generator demo of using next

def gen():
    for i in range(3):
        yield i


for i in gen():
    print(i)


#Assinging generators to the variable and use of next
a=gen()
print(a)
print(next(a))
print(next(a))
print(next(a))
