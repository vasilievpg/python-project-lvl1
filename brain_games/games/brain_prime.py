from math import sqrt
from itertools import count, islice
from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(n):
    if n < 2:
        return False
    # for number in islice(count(2), int(sqrt(n) - 1)):
    for number in range(2, int(sqrt(n) - 1)):
        if not n % number:
            return False
    return True


def get_question_and_answer():
    number = randint(0, 1000)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer
