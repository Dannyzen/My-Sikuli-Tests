#http://stackoverflow.com/questions/4117530/sys-argv1-meaning-in-script
#http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results for ideas on using arparse

#I figure if i write a test app i might as well tell myself wtf i'm doing with these arguments
import argparse
parser = argparse.ArgumentParser(description='This bit takes in commands and builds out docs')
parser.add_argument('-f','--f_variable', help='Description for foo argument', required=True)
parser.add_argument('-b','--b_variable', help='Description for bar argument', required=True)
args = vars(parser.parse_args())

# command line: python cmd_line_args.py -f a -b b
if args['f_variable'] == "a":
    print ("you wrote foo")

if args['b_variable'] == 'b':
    print ("you wrote bar")

"""
import sys
for arg in sys.argv:
	argz = sys.argv[1:]  #ignore sys.argv[0] which is default the scriptname 
print (argz[0],argz[1])
"""