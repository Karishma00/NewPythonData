#List type error

try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print('Type mismatch')

        