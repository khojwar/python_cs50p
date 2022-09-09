
'''
MEOWS = 3

for _ in range(MEOWS):
    print("meow")
'''


'''
class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
    

cat = Cat()
cat.meow()
'''

#---------------------------------------------------------
# type hints
#  mypy - before running python we can check code (eg. mypy <filename.py>) 
# install mypy function (pip install mypy)
#---------------------------------------------------------



'''
def meow(n: int):       # giving hints (ie : int)
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)

# to run this code type in terminal [mypy <file_name>]. 
'''


# it also print none too

'''
def meow(n: int):
    for _ in range(n):
        print("meow")
    
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
'''




'''
def meow(n: int) -> str:
    return "meow\n" *n
    
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
'''


#--------------------------------
# docstrings
#--------------------------------

'''
def meow(n: int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError: if n is not an int
    :return: A string of n meows, one per line
    :rtype: str

    """
    return "meow\n" *n
    
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
'''




#-----------------------------------------------------------------


'''
import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meow.py")
'''




'''
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meow.py")
'''


# use library "argparse"
# argparse means to read it kind of pick it part to analyze it so this is indeed going to do just that for me
# this library helpful to know a little oops like we all now do

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")