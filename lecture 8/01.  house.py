'''
name = input("what's your name? ")

if name == "harry":
    print("gryffindor")
elif name == "hermione":
    print("gryffindor")
elif name == "ron":
    print("gryffindor")
elif name == "draco":
    print("slytherin")
else:
    print("who?")
'''


'''
name = input("what's your name? ")

if name == "harry" or name == "hermione" or name == "ron":
    print("gryffindor")
elif name == "draco":
    print("slytherin")
else:
    print("who?")
'''


#----------------------------------------------------------------------------------------------

# for more compact use "match" same as switch in other language

'''
name = input("what's your name? ")

match name:
    case "harry":
        print("gryffindor")
    case "hermione":
        print("hryffindor")
    case "ron":
        print("gryffindor")
    case "braco":
        print("slytherin")
    case _:
        print("who?")
'''






name = input("what's your name? ")

match name:
    case "harry" | "hermione" | "ron":
        print("gryffindor")
    case "braco":
        print("slytherin")
    case _:
        print("who?")