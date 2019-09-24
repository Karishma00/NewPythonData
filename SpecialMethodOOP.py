#special buit in method used for objects

class Book():
    def __init__(self,name,auther,pages):
        self.name=name
        self.auther=auther
        self.pages=pages

    def __str__(self):
        return f'Book name  : {self.name } Auther :{self.auther}'

    def __len__(self):
        return self.pages

    def __del__(self):#for deletion from memory
        print('Obj deleted..')


b=Book('Pyhton','M.O. Triyas',100)
print(b)
print(len(b))
del b