#Generates the value upon need(Memory efficient)

def cubes(n):
    for i in range(n):
        yield i**3

for i in cubes(15):
    print(i)