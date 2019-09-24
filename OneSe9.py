#Demo for __name__=="__main__"

def fun():
    print("One file function")

print("Top level One Se:9")

if __name__=="__main__":
    print("One Running Directly.")
else:
    print("One Running by Importing.")