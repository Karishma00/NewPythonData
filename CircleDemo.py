#Demo circle


class Circle():

    pi=3.14
    def __init__(self,radius):
        self.radius=radius
        self.area=radius*radius*Circle.pi

    def getCurcum(self):
        return self.radius*self.pi*2

c1=Circle(30)
print(c1.getCurcum())
