# print("hello, world")

#Ask user for their name
name = input("What is your name? ")


#Remove whitespace form str and Capitalize user's name
name = name.strip().title()

# Say hello to user
#print("hello, " + name)
#print("hello,", name)
print(f"hello, {name}")

