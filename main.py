from question_model import Question
from quiz_brain import QuizBrain
from question_sets import sets

def quizGame():
    question_bank = []
    for question in sets:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_got_questions():
        quiz.next_question()
    print("You have reached to the end of this game.")
    print(f"Your current score is {quiz.score}/{quiz.question_number}.")


play_again = True
while play_again:
    quizGame()
    user = input("You want to play QuizGame again? (Yes/No):  ").lower()
    if user == 'no':
        play_again = False
