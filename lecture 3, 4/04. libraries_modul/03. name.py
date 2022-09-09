

'''

import sys

if len(sys.argv) < 2:
    print("Too few arguments ")
elif len(sys.argv) > 2:
    print("Too many argumants ")
else:
    print("hello, my name is ", sys.argv[1])

'''




'''

# it gives IndexError
import sys

if len(sys.argv) < 2:
    print("Too few arguments ")
elif len(sys.argv) > 2:
    print("Too many argumants ")

print("hello, my name is ", sys.argv[1])

'''


'''
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments ")
elif len(sys.argv) > 2:
    sys.exit("Too many argumants ")

print("hello, my name is ", sys.argv[1])
'''




import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments ")

for arg in sys.argv[1:]:
    print("hello, my name is ", arg)
