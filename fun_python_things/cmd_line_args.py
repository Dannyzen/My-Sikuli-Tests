#http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script
#look at http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results for ideas on using arparse


import sys
for arg in sys.argv:
	argz = sys.argv[1:]  #ignore sys.argv[0] which is default the scriptname 
print (argz[0],argz[1])
