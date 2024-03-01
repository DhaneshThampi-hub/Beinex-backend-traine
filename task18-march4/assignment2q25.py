'''25.Quiz Game in Python'''


class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def ask_question(self):
        print(self.text)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(self.options):
                    return user_answer
                else:
                    print("Invalid choice. Please enter a number within the given options.")
            except ValueError:
                print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    total_questions = len(questions)

    print("\nWelcome to the Quiz Game! Answer the following questions:")
    
    for index, question in enumerate(questions, 1):
        print(f"\nQuestion {index}/{total_questions}:")
        user_answer = question.ask_question()
        
        if user_answer == question.correct_option:
            print("Correct! 🎉🏀\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {question.correct_option}. \n")

    print(f"You answered {score} out of {total_questions} questions correctly. Thanks for playing!")

if __name__ == "__main__":
    # Example questions
    question1 = Question("What is the capital of France?", ["Paris", "Berlin", "London"], 1)
    question2 = Question("Which programming language is known for its readability?", ["Java", "Python", "C++"], 2)
    question3 = Question("What is the largest mammal on Earth?", ["Elephant", "Blue Whale", "Giraffe"], 2)

    # Run the quiz
    questions_list = [question1, question2, question3]
    run_quiz(questions_list)
