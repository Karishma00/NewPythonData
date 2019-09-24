#InheritenceDemo and Overriding
class Animal:
    def __init__(self):
        print("Animal created.")
    def who_am_i(self):
        print("Animal ..")
    def eat(self):
        print('Animal eating !')

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created ..')
    def eat(self):
        print('Dog  eating !')

a=Animal()
d=Dog()

print(a.who_am_i(),a.eat())
print(d.who_am_i(),d.eat())
