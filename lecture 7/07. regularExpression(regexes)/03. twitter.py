


'''
url = input("URL: ").strip()
print(url)
'''



'''
# not enough
url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")
'''


'''
# using "re" module

import re

url = input("URL: ").strip()

username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
'''





'''
import re

url = input("URL: ").strip()

matches = re.search("^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(3))
'''



'''
# alternative by using :=

import re

url = input("URL: ").strip()

if matches := re.search("^(https?://)?(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username: ", matches.group(3))
'''



# A | B     either A or B
# (...)     a group
# (?:...)   non-capturing version


'''
# improved alternative 

import re

url = input("URL: ").strip()

matches = re.search("^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(1))
'''




# according to twitter document

from ast import pattern
from posixpath import split
import re
import string
from sys import flags

url = input("URL: ").strip()

matches = re.search("^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print(f"Username: ", matches.group(1))





# some other function

# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flags=0)
