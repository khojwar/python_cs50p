'''
def main():
    yell("This is CS50")
    

def yell(phrase):
    print(phrase.upper())


if __name__ == "__man__":
    main()
'''



# passing list from main function to yell function

'''
def main():
    yell(["This", "is", "CS50"])
    

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__man__":
    main()
'''



#passing string from main functio to yell function
'''
def main():
    yell("This", "is", "CS50")
    

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__man__":
    main()
'''



#-----------------------------
# using map functio 
#----------------------------

'''
def main():
    yell("This", "is", "CS50")
    

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__man__":
    main()

'''
#-----------------------------------
#   list comprehensions
#-----------------------------------


def main():
    yell("This", "is", "CS50")
    

def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__man__":
    main()

