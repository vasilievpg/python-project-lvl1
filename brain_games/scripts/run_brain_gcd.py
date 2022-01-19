#!/usr/bin/env python

import brain_games.games.brain_gcd
from brain_games.scripts.game_logic import game_logic


def brain_gcd():
    game_logic(brain_games.games.brain_gcd)


def main():
    brain_gcd()


if __name__ == "__main__":
    main()
