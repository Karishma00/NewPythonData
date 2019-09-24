#Exception handling with addtion of strings
result=0
try:
    n1=int(input('Enter no1 :'))
    n2=int(input('Enter no2 :'))
    result=n1+n2

except:
    print('Please enter number ....')
else:
    print('The sum is :',result)

