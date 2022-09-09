'''
name = input("what's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
'''


'''
name = input("what's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
'''

'''
# using with not need to close file
name = input("what's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
'''

# read file

'''
with open("names.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    print("hello, ", line, end="")   # end="" remove the extra line
'''




'''
with open("names.txt", "r") as file:
    lines = file.readlines()


for line in lines:
    print("hello, ", line.rsplit())
'''


'''
# more compact way but not sorted
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
'''



# more compact and sorted
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
# for name in sorted(names, reverse=True):
    print(f"hello, {name}")

