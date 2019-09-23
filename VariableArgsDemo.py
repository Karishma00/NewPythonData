#Variable arguments uses the tuple


def vrgsd(*args):
    return sum(args)


print('Sum is :',vrgsd(10,20,40))
