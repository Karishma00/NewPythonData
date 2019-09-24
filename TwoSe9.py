
#One file is imported and called
import OneSe9
def fun1():
    print("Two file function")

print("Top level in Two - One Se:9")
OneSe9.fun()

if __name__=="__main__":
    print("Two Running Directly.")
else:
    print("Two Running by Importing.")