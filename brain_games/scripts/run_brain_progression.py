#!/usr/bin/env python

import brain_games.games.brain_progression
from brain_games.scripts.game_logic import game_logic


def brain_progression():
    game_logic(brain_games.games.brain_progression)


def main():
    brain_progression()


if __name__ == "__main__":
    main()
