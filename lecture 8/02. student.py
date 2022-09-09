'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")



def get_name():
    return input("Name: ")



def get_house():
    return input("House: ")




if __name__ == "__main__":
    main()
'''




'''
def main():
    name, house = get_student()
    print(f"{name} from {house}")



def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
'''




'''
# using tuple is not mutable

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
'''



'''
# using list ismutable

def main():
    student = get_student()
    if student[0] == "padma":
        student[1] = "ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main()
'''



# using "dict"  is better 

'''
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main()
'''




# more compact way 

'''
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''






# dict is mutable

'''
def main():
    student = get_student()
    if student["name"] == "padma":
        student["house"] = "ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
'''




# using class 

'''
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()     #objects
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
'''





'''
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    # student = Student(name, house)      # constructing object
    # return student
    return Student(name, house)


if __name__ == "__main__":
    main()
'''





'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''




# other way

'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''





# using build in function 

'''
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    
    def charm(self):
        if self.patronus == "Stag":
            return "😀"
        elif self.patronus == "Otter":
            return "😅"
        elif self.patronus == "Jack Russell terrier":
            return "😍"
        else:
            return "🐻"
    


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
'''





'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''






'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''





'''
# it gives error
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    def house(self):
        return self.house
    

    # Setter
    def house(self, house):
        self.house = house

def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''



# using property (Decorator (getter , setter))

'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property   # Getter
    def house(self):
        return self._house
    

    @house.setter       # Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
'''








class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property   # Getter
    def house(self):
        return self._house
    

    @house.setter       # Setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()




#----------------------------------------------------------------------
# Everything related to student in the student class more manage way
#-----------------------------------------------------------------------


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)     # creating object of current class
    

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()