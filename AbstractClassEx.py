#Abstract class example

class Animal():
    def __init__(self, name):
        print("Animal ..")
        self.name = name

    def speak(self):
        raise  NotImplementedError("Subclass has to implemnt that .")

class Dog(Animal):
    def __init__(self, name):
        print("Dog ..")
        self.name = name

    def speak(self):
        return self.name +'  speak Woof..'


class Cat(Animal):
    def __init__(self,name):
        print("Cat ..")
        self.name=name

    def speak(self):
        return self.name +'  speak Woof..'


d=Dog('Rozer')
c=Cat('Tom')
print(d.speak())
print(c.speak())

#

