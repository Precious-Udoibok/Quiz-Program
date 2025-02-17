
class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_number(self):
        '''returns True if the number of questions the users has anser is less than the questions
        in the list'''
        number_of_questions = len(self.question_list)
        return self.question_number < number_of_questions

    def next_question(self):
        '''gives the user the next questions and checks the answer'''
        current_question = self.question_list[self.question_number]
        self.question_number+= 1
        user_answer = input(f'Q.{self.question_number}: {current_question.text}? (True/False): ')
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        '''Check the user answer against the correct answer'''
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right')
        else:
            print(f'You got it wrong')
        print(f'The correct answer is {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print('\n')