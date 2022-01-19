#!/usr/bin/env python

import brain_games.games.brain_prime
from brain_games.scripts.game_logic import game_logic


def brain_prime():
    game_logic(brain_games.games.brain_prime)


def main():
    brain_prime()


if __name__ == "__main__":
    main()
