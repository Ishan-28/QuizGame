from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# Iterating items through the question_data list which contains a list of dictionaries
question_bank = []
for question_set in question_data:
    question_text = question_set["text"]
    question_answer = question_set["answer"]
    problem = Question(question_text, question_answer)
    question_bank.append(problem)

quiz = QuizBrain(question_bank)

while quiz.still_got_question:
    quiz.next_question()
