#!/usr/bin/env python

from brain_games.scripts.cli import welcome_user
from brain_games.scripts.brain_even import brain_vevn


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    brain_vevn(name)


if __name__ == '__main__':
    main()
