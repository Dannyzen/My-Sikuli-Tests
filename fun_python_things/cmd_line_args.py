#http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script

import sys
for arg in sys.argv:
	argz = sys.argv[1:]  #ignore sys.argv[0] which is default the scriptname 
print (argz[1])