
'''
try:
    x = int(input("what's x?"))
    print(f"x is {x} ")
except ValueError:
    print("x is not an integer")
'''


'''
try:
    x = int(input("what's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x} ")
'''


'''
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x} ")

'''


'''
# using def function
def main():
    x = get_int()
    print(f"x is {x} ")


def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()

'''


'''
# alternative (return x can act as break and return value)
def main():
    x = get_int()
    print(f"x is {x} ")


def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x
    


main()

'''


'''
# more compact way
def main():
    x = get_int()
    print(f"x is {x} ")


def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
    


main()

'''



'''
# alternative using pass
def main():
    x = get_int()
    print(f"x is {x} ")


def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass
    


main()

'''





#more dynamic way
def main():
    x = get_int("what's x? ")
    print(f"x is {x} ")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
    


main()