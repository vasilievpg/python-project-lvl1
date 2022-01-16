#!/usr/bin/env python

from random import randint
from brain_games.scripts.compare_answer import compare_answer


def func_answer():
    num_1 = randint(1, 100)
    num_2 = randint(1, 100)
    question = f"{num_1} {num_2}"
    divider = num_1 if num_1 <= num_2 else num_2
    for _ in range(divider):
        if num_1 % divider == 0 and num_2 % divider == 0:
            return question, str(divider)
        else:
            divider -= 1

    return question, "1"


def brain_gcd():
    text_conditions = "What is the result of the expression?"
    compare_answer(func_answer, text_conditions)


def main():
    brain_gcd()


if __name__ == "__main__":
    main()
