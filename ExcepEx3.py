#Ask for int and continue and print square
def ask():
    while True:
        try:
            a=(int(input('Enter number : ')))
        except:
             #print('Not number try again ....')
             continue
        else:
              print('The Square is  :',a**2)
              break

ask()

