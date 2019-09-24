#New decorator to add functionality to function

def new_decorator(exist_f):
    def Wrapping():
        print('Before Wrap')
        exist_f()
        print('After Wrapping the function by code ..')
    return Wrapping()




#By applying using @
@new_decorator
def Original_fun():
    print('I want some extra decoration.')

#this are befor @applying
#Call to the function
#Original_fun()

#Applying the decorator
#new_decorator(Original_fun)





