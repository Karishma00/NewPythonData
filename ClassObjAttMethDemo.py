#class Object Attribute and method demo
class  Dog():
    # class obj attribute is same for all the obj
    species='mammal'

    def __init__(self,breed,name,spot):
        self.breed=breed
        self.name=name
        self.spot=spot

    def bark(self):
        print('Woof ..')

d1=Dog('lab','Tomy','yes')
d2=Dog('Cab','Rozer','No')
print("D1 Obj")
print(d1.breed,d1.name,d1.species,d1.bark())

print("D2 Obj")
print(d2.breed,d2.name,d2.species,d2.bark())



