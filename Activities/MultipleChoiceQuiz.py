#class
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

#arrays / Objects
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "WHat color are Strawberies?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#calling the class using array
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

#function
def run_Test(ques):
    score = 0
    for every_question in ques:
        answer = input(every_question.prompt + "Your answer is: ")
        if answer == every_question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(ques)) + " correct")

run_Test(questions)