#String IO Basically for i/p o/p and treat the strings like file

import io
msg = 'String IO example '

f=io.StringIO(msg)
print(f.read())
f.write('Writing the text')
f.seek(0)
print(f.read())
f.close()