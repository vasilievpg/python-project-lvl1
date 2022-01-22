from random import randint

DESCRIPTION = ('Answer "yes" if given number is prime.'
               ' Otherwise answer "no".')


def is_prime(number):
    answer = True

    if number < 2:
        answer = False

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            answer = False

        divider += 1

    return answer


def get_question_and_answer():
    number = randint(0, 1000)
    question = str(number)
    dict_answers = {True: 'yes', False: 'no'}
    answer = dict_answers[is_prime(number)]

    return question, answer
