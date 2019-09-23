#OOP example demo Class and attributes

class Student():

    def __init__(self,sid,sname):
        self.sid=sid
        self.sname=sname

s1=Student(sid='101',sname='Rina')
print(s1.sid)
print(s1.sname)

