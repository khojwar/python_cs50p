#_-------------------------------
#  Global variable
#---------------------------------

'''
balance = 0

def main():
    print("Balance:", balance)


if __name__ == "__main__":
    main()
'''


# Global variable - we need to define global
'''
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n



if __name__ == "__main__":
    main()
'''



# oops concepts in the same program

class Account:
    def __init__(self):
        self._balance = 0       # instance variable, it can be accessible by all the method inside class

    @property                   # instant variable (getter - we can print in the main function || setter - we can assign value in the main function) 
    def balance(self):
        return self._balance
    

    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n
    

def main():
    account = Account()         # constructor (creating the object)
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)



if __name__ == "__main__":
    main()