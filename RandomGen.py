#Exercise of generators 12 numbers

from random import randint
def RanGen(l,h,num):
    for i in range(num):
        a=yield randint(l,h)
    return a
print(list(RanGen(1,10,12)))


