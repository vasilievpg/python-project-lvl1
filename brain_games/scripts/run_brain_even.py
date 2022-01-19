#!/usr/bin/env python

import brain_games.games.brain_even
from brain_games.scripts.game_logic import game_logic


def brain_even():
    game_logic(brain_games.games.brain_even)


def main():
    brain_even()


if __name__ == "__main__":
    main()
