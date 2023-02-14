from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    question_obj = Question(data["question"], data["correct_answer"])
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    try:
        quiz.next_question()

    except KeyboardInterrupt:
        print("\nExiting program...")
        break

print("\n\nYou've completed the quiz!")
print(f"Your final score was: {quiz.get_final_score()}")
