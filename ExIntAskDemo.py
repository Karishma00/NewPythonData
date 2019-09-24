#Ask for int and continue
def ask():
    while True:
        try:
            a=(int(input('Enter number : ')))
        except:
             print('Not number try again ....')
             continue
        else:
              print('The number is  :',a)
              break
        finally:
              print('Done ! finally')

ask()

