#!/usr/bin/env python

from random import randint, choice

from brain_games.scripts.cli import compare_answer


def func_question():

    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operations = ('+', "-", '*')
    operation = choice(operations)

    return (f"{num_1} {operation} {num_2}")


def func_correct_answer(question):
    return str(eval(question))


def brain_calc():
    text_conditions = ('What is the result of the expression?')
    compare_answer(func_question, func_correct_answer, text_conditions)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
