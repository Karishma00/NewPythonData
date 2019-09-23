def check(st):
    if 'a' in st:
        return ("Valid String")
    else:
        return("Not valid")

s=input('Enter string :')
print(s,check(s))