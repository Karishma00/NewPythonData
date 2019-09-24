#Calling the created modules

from Module import  myfunc
#from folders import py files
from PackageMain import MainPkgScript
from PackageMain.PackageSub import SubPkgScript

#calling the module
print('In the Program ')
myfunc()

#Calling the function of folders
print('Calling the main package !!')
MainPkgScript.MainReport()
print('Calling the Sub package')
SubPkgScript.subReport()


