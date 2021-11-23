#!/usr/bin/env python

from brain_games.scripts.cli import welcome_user
from brain_games.scripts.brain_even import brain_even
from brain_games.scripts.brain_even import conditions


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    conditions()
    brain_even(name)


if __name__ == '__main__':
    main()
