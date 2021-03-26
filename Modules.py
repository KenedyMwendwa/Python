#we can use done completed modules in python to write our codes
#basically they are stored under external libraries, exte\

from Student import Student
student1 = Student("sama", "coding", 2.0, True)
student2 = Student("sam", "design", 2.0, True)
student3 = Student("meshack", "coding", 3.0, True)
student4 = Student("brian", "coding", 2.0, False)
print(student1.name)
print(student2.major)
print(student3.gpa)
print(student4.is_on_probation)
