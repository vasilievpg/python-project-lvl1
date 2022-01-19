from random import randint

text_conditions = "What is the result of the expression?"


def find_divider(num_1, num_2):
    divider = num_1 if num_1 <= num_2 else num_2
    for _ in range(divider):
        if num_1 % divider == 0 and num_2 % divider == 0:
            return str(divider)
        else:
            divider -= 1


def get_question_and_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f"{num_1} {num_2}"
    divider = find_divider(num_1, num_2)

    return question, divider
