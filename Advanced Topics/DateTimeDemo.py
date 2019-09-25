
import datetime
d=datetime.time(10,20,45)
print(d)

today= datetime.date.today()
print(today)
print(datetime.date.max)
print(datetime.date.min)
print(today.timetuple())
print(today.weekday())
print(datetime.date.resolution)

#Replacing
d1=datetime.date(2019,6,23)
print(d1)
d2=d1.replace(month=4,day=13,year=1970)
print('Replaced d1 : ',d2)

#Arithmatic
print(d1-d2)
