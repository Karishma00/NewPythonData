x = 50
def myfun():
    #global x Now this x will be global
    x=22
    print(x)
    def fun():
        x = 7
        print(x)
    fun()


print(myfun())
print(x)


