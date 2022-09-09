


'''
name = input("what's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
'''



# A | B     either A or B
# (...)     a group
# (?:...)   non-capturing version




# using "re" module

'''
import re

name = input("What's your name? ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"
print(f"hello, {name}")
'''




'''
import re

name = input("What's your name? ").strip()
matches = re.search("^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")
'''



'''
# alternative
import re

name = input("What's your name? ").strip()
matches = re.search("^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
'''



# using walrus operator (:=) for more compact

import re

name = input("What's your name? ").strip()
if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

