'''
#dataType
#int
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
'''

'''
#float
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)   #syntax:- round(number[, ndigits])

print(f"{z:,}")

'''

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x/y, 2)   #syntax:- round(number[, ndigits])
print(f"{z:.2f}")
print(z)