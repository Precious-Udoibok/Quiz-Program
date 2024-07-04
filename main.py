from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] #A LIST TO STORE THE QUESTION BANK

#loop through the questions in question data
#and creating question objects and appending it to the question list
for questions in question_data:
    question_text = questions['question']
    question_answer = questions['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_number():
    quiz.next_question()
print('You have completed the quiz challenge')
print(f'Your final score is {quiz.score}/{quiz.question_number}')