#-----------------------------------------------
#       list conprihention
#-----------------------------------------------

'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},

]



gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
'''





# ----------------------------------------
#       filter
#-----------------------------------------

'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},

]


def is_gryffindor(s):
    # if s["house"] == "Gryffindor":
    #     return True
    # else:
    #     return False
    return s["house"] == "Gryffindor"



gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])

'''


# alternative but same approach



'''
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},

]


def is_gryffindor(s):
    # if s["house"] == "Gryffindor":
    #     return True
    # else:
    #     return False
    return s["house"] == "Gryffindor"



gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryffindor["name"])
'''





#------------------------------------
#       dictionary comprehension
#------------------------------------

'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = []


for student in students:
    gryffindors.append({"name": student, "house": "Griffindor"})

print(gryffindors)

'''

# compact way
'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = [{"name": student, "house": "Gryffindor" } for student in students]


print(gryffindors)
'''


'''
students = ["Hermione", "Harry", "Ron"]

gryffindors = {student : "Gryffindor" for student in students }


print(gryffindors)
'''  



#-----------------------------------------------------------------------------


'''
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])
'''


#------------------------------------
#       enumerate     --> key: value dubai laai linxa as variable || index ra value laai variable ko rup maa linxa
#------------------------------------



students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i+1, students[i])





