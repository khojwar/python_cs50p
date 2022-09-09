'''
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
'''


'''
# making more readable 

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
'''


'''
# arranging in assending order
students = []


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
'''







'''
students = []


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
'''


'''
# alternative

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
'''



'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]


#for student in sorted(students, key=get_name):
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")
'''



'''
# alternative using lambda
students = []


with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
'''






'''
# instead above code we recomend you to import csv moduol

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})


for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is rom {student['home']}")
'''




'''
# alternative and readable
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})


for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is rom {student['home']}")
'''


'''
# for csv.DictReader  play video on 03:03 hr

import csv

students =[]

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key= lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
'''



import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})