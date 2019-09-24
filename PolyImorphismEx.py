#Polymorphism demo by two classes
class Dog():
    def __init__(self,name):
        print("dog ..")
        self.name=name
    def speak(self):
        return self.name +'  speak Woof..'


class Cat():
    def __init__(self,name):
        print("Cat ..")
        self.name=name

    def speak(self):
        return self.name +'  speak Woof..'

d=Dog('Tomy')
c=Cat('Tery')
print(d.speak())
print(c.speak())

#Another  way to iterate throug loop
for i in [d,c]:
    print(type(i))
    print(type(i.speak()))


#By fuuction
def pet(p):
    print(p.speak())

pet(d)
pet(c)


