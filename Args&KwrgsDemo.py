

#Both

def printing(*args,**kwargs):
    print(args)
    print(kwargs)

    print('Args is : {}  and Kwrgs is : {}'.format(args[1],kwargs['a']))


printing(10,20,30,a='A',b='b')