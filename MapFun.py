#Lambda and map and fileter function


def square (num):
    return num **2

list=[1,2,3,4,5]
for i in map(square,list):
    print(i)