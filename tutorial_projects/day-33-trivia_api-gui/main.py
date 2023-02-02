from question_model import Question
from data import get_random_questions
from quiz_brain import QuizBrain
from html import unescape
from ui import QuizInterface


question_bank = []
for question in get_random_questions():
    question_text = unescape(question["question"])
    question_answer = unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
window = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
