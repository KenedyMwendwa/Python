#we import the class containing the attributes of desired objects
#from Student import Questions
class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "what color are apples?\n(a) Red\Green\n(b) Purple\n(c) Orange\n\n",
    "what color are bananas?\n(a) Tea\n(b) Purple\n(c) Yellow\n\n",
    "what color are unripe mangoes?\n(a) Yellow\n(b) Red\n(c) Green\n\n"
]
#create the objects of the question
questions = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "c"),
]
def run_test(questions):
     score = 0
     for question in questions:
         answer = input(question.prompt)
         if answer == question.answer:
             score += 1
     print("You got " + str(score) + "/" + str(len(questions)) + "correct" )

run_test(questions)