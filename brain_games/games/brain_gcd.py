from random import randint

DESCRIPTION = 'What is the result of the expression?'


def find_gcd(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return max(num_1, num_2)
    else:
        if num_1 > num_2:
            return find_gcd(num_1 % num_2, num_2)
        else:
            return find_gcd(num_1, num_2 % num_1)


def get_question_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f'{num_1} {num_2}'
    answer = str(find_gcd(num_1, num_2))

    return question, answer
