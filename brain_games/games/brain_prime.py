#!/usr/bin/env python

from random import randint
from brain_games.scripts.compare_answer import compare_answer


def func_answer():
    number = randint(0, 1000)
    question = str(number)
    correct_answer = "yes"

    if number < 2:
        correct_answer = "no"

    divider = 2

    while divider <= number / 2:
        if number % divider == 0:
            correct_answer = "no"

        divider += 1

    return question, correct_answer


def brain_prime():
    text_conditions = 'Answer "yes" if given number is prime. ' 'Otherwise answer "no".'
    compare_answer(func_answer, text_conditions)


def main():
    brain_prime()


if __name__ == "__main__":
    main()
