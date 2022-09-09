
'''
import sys
import saying

if len(sys.argv) == 2:
    saying.goodbye(sys.argv[1])
'''



import sys
from saying import hello, goodbye

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])
    