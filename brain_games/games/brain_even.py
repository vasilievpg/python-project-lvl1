#!/usr/bin/env python

from random import randint
from brain_games.scripts.compare_answer import compare_answer


def func_question():
    return randint(1, 100)


def func_correct_answer(question):
    return 'yes' if question % 2 == 0 else 'no'


def brain_even():
    text_conditions = ('Answer "yes" if the number is even, '
                       'otherwise answer "no".')
    compare_answer(func_question, func_correct_answer, text_conditions)


def main():
    brain_even()


if __name__ == '__main__':
    main()
