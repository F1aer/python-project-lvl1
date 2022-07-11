import random

rules = 'Answer "yes" if the number is even, otherwise answer "no".'

lower_char = 1
upper_char = 100


def is_even(number):
    return number % 2 == 0


def get_correct_answer_and_question():
    number = random.randint(lower_char, upper_char)
    if is_even(number):
        result = "yes"
    else:
        result = "no"
    question = str(number)
    return result, question
