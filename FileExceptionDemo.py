#File operation Exception demo

try:
    f=open('wr.txt','r')
    f.write('Hello  !!!')

    print(f.read())
except:
    print('Not writable')
finally:
    f.close()

