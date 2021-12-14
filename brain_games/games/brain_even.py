#!/usr/bin/env python

from random import randint
from brain_games.scripts.compare_answer import compare_answer


def func_answer():
    question = randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'

    return question, correct_answer


def brain_even():
    text_conditions = ('Answer "yes" if the number is even, '
                       'otherwise answer "no".')
    compare_answer(func_answer, text_conditions)


def main():
    brain_even()


if __name__ == '__main__':
    main()
