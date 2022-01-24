from random import randint

DESCRIPTION = 'What is the result of the expression?'


def gcd(p: int, q: int) -> int:
    while q != 0:
        (p, q) = (q, p % q)
    return p


def get_question_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f'{num_1} {num_2}'
    answer = str(gcd(num_1, num_2))

    return question, answer
