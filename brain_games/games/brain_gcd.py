#!/usr/bin/env python

from random import randint

from brain_games.scripts.compare_answer import compare_answer


def func_answer():
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    question = f"{num_1} {num_2}"
    num1, num2 = question.split(' ')
    num1 = int(num1)
    num2 = int(num2)
    # correct_answer =

    return (question, correct_answer)


def brain_gcd():
    text_conditions = ('What is the result of the expression?')
    compare_answer(func_answer, text_conditions)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
