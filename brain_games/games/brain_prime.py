from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(number):
    if number % 2 == 0:
        return number == 2
    divider = 3
    while divider * divider <= number and number % divider != 0:
        divider += 2
    return divider * divider > number


def get_question_and_answer():
    number = randint(0, 1000)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'

    return question, answer
