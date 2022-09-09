students = [
    {"name": "hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russell terrier"},
    {"name": "draco", "house": "slytherin", "patronus": None}

]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")