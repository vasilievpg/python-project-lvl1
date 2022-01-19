#!/usr/bin/env python

from random import randint, choice
from brain_games.scripts.game_logic import game_logic


def get_question_and_answer():
    correct_answer = 0
    num_1 = randint(1, 10)
    num_2 = randint(1, 10)
    operations = ('+', '-', '*')
    operation = choice(operations)
    question = f"{num_1} {operation} {num_2}"
    if operation == '+':
        correct_answer = num_1 + num_2
    elif operation == '-':
        correct_answer = num_1 - num_2
    elif operation == '*':
        correct_answer = num_1 * num_2

    return question, str(correct_answer)


def brain_calc():
    text_conditions = 'What is the result of the expression?'
    game_logic(get_question_and_answer, text_conditions)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
