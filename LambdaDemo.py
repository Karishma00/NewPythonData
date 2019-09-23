#lamda with map and filter


square = lambda n:n **2


print(square(10))

#Using Map
l=[3,5,7,9,10]

a=list(map(lambda n:n **2,l))
print(a)

#Using filter
b=list(filter(lambda n:n%2==0,a))
print(b)

#print 1st char
names=['Abc','Mno','Xyz']
l2=list(map(lambda a:a[0],names))
print(l2)

#Print 1st char
l3=list(filter(lambda a:a!=0,names))
print(l3)

