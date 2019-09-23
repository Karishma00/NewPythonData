#Ues the dictionaries

def checking(**kwargs):
    if 'fruit' in kwargs:
        print('The fruit is : {}'.format(kwargs['fruit']))
    else:
        print("Nothing ..")

checking(fruit='apple')




