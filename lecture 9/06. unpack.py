'''
first, _ = input("what's your name? ").split(" ")
print(f"hello, {first}")
'''


'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(100, 50,25), "knuts")
'''



# passing parameter using list
'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(coins[0], coins[1], coins[2]), "knuts")
'''

#-------------------------------
# using "unpack list" for above same program :- (* is use for unpack)
#-------------------------------

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "knuts")
'''

#-----------------------------------------
# using dict to pass argument
#-----------------------------------------

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
'''


# using "unpack dict" to pass argument (**)

'''
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")   # it is same as print(total(galleons=100, sickles=50, knuts=25), "Knuts")   

'''





#--------------------------------------------
#   *args, **kwargs       not like above program, it is for you can pass any number of arguments
#--------------------------------------------


'''
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)
f(100, 50, 25, 5)
f(5)
'''



def f(*args, **kwargs):
    print("Named: ", kwargs)

f(galleons=100, sickles=50, knuts=25)

