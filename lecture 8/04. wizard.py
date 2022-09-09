# inheritance

'''
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
'''




class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student:
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    
    ...


class Professor:
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    ...

wizard = Wizard("Albus")
student = Student("Harry")
professor = Professor("Severus")