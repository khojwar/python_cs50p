'''
def main():
    name = input("what's your name? ")
    hello(name)


def hello(to="world"):     
    print("hello, ", to)   # test garna ko laagi return lekhna parxa


if __name__ == "__main__":
    main()
'''



def main():
    name = input("what's your name? ")
    print(hello(name))


def hello(to="world"):     
    return f"hello, {to}"   # test garna ko laagi return lekhna parxa


if __name__ == "__main__":
    main()