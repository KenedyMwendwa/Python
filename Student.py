#we can create class of our own choice
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa =gpa
        self.is_on_probation = is_on_probation

#after passing the attributes of our object, we can import this code and used it different parta
#create another class for question and answer game
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

