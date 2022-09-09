'''
email = input("What's your email? ").strip()

if "@" in email and "." in email: 
    print("Valid")
else:
    print("Invalid")
'''



'''
# still something is missing

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("valid")
else:
    print("Invalid")
'''



'''
# still not enough

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("Invalid")
'''




# use "re" modul 



# some important Symbols
# .     any character except a newline
# *     0 or more repetitions
# +     1 or more repetitions
# ?     0 or 1 repetition
# {m}   m repetitions
# {m,n} m-n repetitions

# ^     matches the start of the string
# $     matches the end of the string or just before the newline at the end of the string

# []    set of characters
# [^]     complementing the set



'''
# not enough

import re

email = input("What's your email? ").strip()

if re.search("^.+@.+\.edu$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''



'''
import re

email = input("What's your email? ").strip()

if re.search("^[^@]+@[^@]+\.edu$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''



'''
# alternative 

import re

email = input("What's your email? ").strip()

if re.search("^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''




    # \d    decimal digit
    # \D    not a decimal digit
    # \s    whithespace characters
    # \S    not a whitespace characters
    # \w    word character...as well as numbers and the undersore
    # \W    not a word character


'''
# alternative more readable

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.edu$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")

'''


# A|B       either A or B
# (...)     a group
#(?:...)    non-capturing version



'''
# alternative 

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.(com|edu|gov|net|org)$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''





'''
# alternative and lower care

import re

email = input("What's your email? ").strip().lower()

if re.search("^\w+@\w+\.(com|edu|gov|net|org)$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''





'''
# alternative and lower care

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.(com|edu|gov|net|org)$", email.lower()):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''




'''
# alternative and lower care

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.(com|edu|gov|net|org)$", email):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''



# re.IGNORECASE
# re.MULTILINE
# re.DOTALL



'''
# alternative and take user input same as input

import re

email = input("What's your email? ").strip()

if re.search("^\w+@\w+\.edu$", email, re.IGNORECASE):  #alternative if re.search("..*@..*\.edu", email):
    print("Valid")
else:
    print("Invalid")
'''




# for both tika@hardvard.edu and tika@cs50.hardvard.edu

import re

email = input("What's your email? ").strip()

if re.search("^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):  
    print("Valid")
else:
    print("Invalid")






