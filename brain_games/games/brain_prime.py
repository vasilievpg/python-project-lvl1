from random import randint

text_conditions = ('Answer "yes" if given number is prime.'
                   ' Otherwise answer "no".')


def checking_number_for_prime(number):
    answer = "yes"

    if number < 2:
        answer = "no"

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            answer = "no"

        divider += 1

    return answer


def get_question_and_answer():
    number = randint(0, 1000)
    question = str(number)
    correct_answer = checking_number_for_prime(number)

    return question, correct_answer
