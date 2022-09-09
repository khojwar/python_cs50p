# students = ["hermione", "Harry", "Ron"]

# for student in students:
#     print(student)


# for i in range(len(students)):
#     print(i + 1, students[i])


# dictionary
students = {
    "hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

# print(students["hermione"])

for student in students:
    print(student, students[student], sep=", ")