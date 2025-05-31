
import random, math


def randomNumber(min, maximum):
    return random.randint(min, maximum)

class MathQuestion:
    operations = [op for op in ["addition", "subtraction", "square_root", "linear_equation"]]

    def __init__(self, title, type, number1, number2):
        self.title = title
        self.type = type
        self.number1 = number1
        self.number2 = number2
        self.correct_answer = None
        self.generate_question()

    def generate_question(self):
        if self.type == 'addition':
            self.title = f"What is {self.number1} + {self.number2}?"
            self.correct_answer = self.number1 + self.number2

        elif self.type == 'subtraction':
            self.title = f"What is {self.number1} - {self.number2}?"
            self.correct_answer = self.number1 - self.number2

        elif self.type == 'square_root':
            self.title = f"What is the square root of {self.number1}?"
            self.correct_answer = math.sqrt(self.number1)

        elif self.type == 'linear_equation':
            # format: ax + b = cx + d
            a = self.number1
            c = self.number2
            b = randomNumber(1, 10)
            d = randomNumber(1, 10)
            self.title = f"Solve for x: {a}x + {b} = {c}x + {d}"
            denominator = a - c
            if denominator != 0:
                self.correct_answer = (d - b) / denominator
            else:
                self.correct_answer = 0 
                


def run_math_quiz():
    print("Starting math quiz")
    score = 0
    
    total_questions = int(input("How many questions do you want? "))
    

    for i in range(total_questions):
        num1 = randomNumber(1, 10)
        num2 = randomNumber(1, 10)
        random_topic = random.choice(MathQuestion.operations)
        question = MathQuestion("Template", f"{random_topic}", num1, num2)

        try:
            user_answer = float((input(f"{question.title} ")))
            if user_answer == float(question.correct_answer):
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. The correct answer was {question.correct_answer}.\n")
        except ValueError:
            print("Invalid input. Question counted as incorrect.\n")

    print(f"Quiz Complete! You scored {score} out of {total_questions}.\n")


quizzes = {
    'math': run_math_quiz,
}

while True:
    choice = input("What type of quiz? (math) ").lower()
    if choice in quizzes:
        print(f"Picked {choice} quiz")
        quizzes[choice]()
        break
    else:
        print("Quiz not available. Available tests: Math")
