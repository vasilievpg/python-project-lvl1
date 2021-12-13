#!/usr/bin/env python

from random import randint, choice
from brain_games.scripts.compare_answer import compare_answer


def func_answer():
    global correct_answer
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operations = ('+', "-", '*')
    operation = choice(operations)
    question = f"{num_1} {operation} {num_2}"
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2

    return (question, str(correct_answer))


def brain_calc():
    text_conditions = 'What is the result of the expression?'
    compare_answer(func_answer, text_conditions)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
