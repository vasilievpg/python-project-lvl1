#!/usr/bin/env python

from random import randint

from brain_games.scripts.cli import welcome_user, conditions, compare_answer
from brain_games.scripts.cli import congratulations


def brain_even(name):
    i = 1
    while i <= 3:
        question = randint(1, 100)
        correct_answer = 'yes' if question % 2 == 0 else 'no'
        if compare_answer(question, correct_answer, name):
            i += 1
        else:
            return False
    congratulations(name)


def main():
    name = welcome_user()
    conditions('Answer "yes" if the number is even, otherwise answer "no".')
    brain_even(name)


if __name__ == '__main__':
    main()
