#Defining and returning the function to another

def one():
    def two():
        print('In second function..')
    return two()


print('In first function..')
one()



