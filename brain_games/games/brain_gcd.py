#!/usr/bin/env python

from random import randint

from brain_games.scripts.compare_answer import compare_answer


def func_question():

    num_1 = randint(1, 10)
    num_2 = randint(1, 10)

    return (f"{num_1} {num_2}")


def func_correct_answer(question):
    num1, num2 = question.split(' ')
    num1 = int(num1)
    num2 = int(num2)
    print(f"Число 1: {num1}")
    print(f"Число 2: {num2}")


def brain_gcd():
    text_conditions = ('What is the result of the expression?')
    compare_answer(func_question, func_correct_answer, text_conditions)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
