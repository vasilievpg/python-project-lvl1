from math import sqrt
from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(number):
    if number < 2:
        return False
    for divider in range(2, int(sqrt(number) - 1)):
        if number % divider == 0:
            return False
    return True


def get_question_and_answer():
    number = randint(0, 1000)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer
