from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():
    answer = 0
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
    }
    operation = choice(list(operations))
    question = f"{num_1} {operation} {num_2}"
    answer = operations[operation](num_1, num_2)

    return question, str(answer)
