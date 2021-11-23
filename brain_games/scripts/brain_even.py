#!/usr/bin/env python

import prompt
from random import randint

from brain_games.scripts.cli import welcome_user


def conditions():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def brain_even(name):
    i = 1
    while i <= 3:
        random_number = randint(1, 100)
        correct_answer = 'yes' if random_number % 2 == 0 else 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return name
    print(f"Congratulations, {name}!")


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()