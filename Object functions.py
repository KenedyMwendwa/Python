class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
#we can define functions to be used by different  objects inside the program


student1=(Student("Mulila", "Coder", 3.4))
student2= (Student("Mwelu", "Statistician", 3.88))
student3= (Student("Muuo", "Programmer", 3.88))
print(student1.on_honor_roll())
print(student2.on_honor_roll())
print(student3.on_honor_roll()) 