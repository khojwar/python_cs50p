#------------------------------------
#       generators          --> in stead of using return, use yield. Large size input may causes code crash. Because return generate all data at a time but yield generate little bit of date at a time 
#------------------------------------

'''
n = int(input("What's n? "))
for i in range(n):
    print("🐑" * i)
'''




'''
def main():
    n = int(input("What's n? "))
    for i in range(n):
        print(sheep(i))


def sheep(n):
    return "🐑" * n


if __name__ == "__main__":
    main()
'''




'''
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock


if __name__ == "__main__":
    main()
'''




# above breaks when code breaks when we put more than 100,000 as n. So we need generator as solution of this problem. ie yield






#------------------------------------
#      yield        --> return one value at a time
#------------------------------------

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()







#------------------------------------
#       iterators
#------------------------------------







