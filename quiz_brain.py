class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list

    def still_got_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}) {current_question.text} (True/False).\nYour answer: ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("You got it right!!!")
        else:
            print("Sorry, but you are wrong..")
        print(f"The correct answer is {correct_answer}.")
