"""
Main module of the game
"""
import sys

from exceptions import GameOver, EnemyDown
from models import Player
from models import Enemy
from settings import ALLOWED_COMMANDS


def play():
    """
    Accepts a username, displays a greeting and passes the username to the function 'start_play'.
    """
    name = input('Enter your name:')
    print("_" * 33)
    print("Hello {}!".format(name))
    print("¯" * 33)
    start_play(name)


def start_play(name):
    """
    The main function that contains the logic of the game/
    """
    player_command = None
    while player_command not in ALLOWED_COMMANDS:
        player_command = input("+++++++++++++++++++++++++++++++++\n"
                               "+  Enter START to start game.   +\n"
                               "+  Enter HELP to see commands.  +\n"
                               "+++++++++++++++++++++++++++++++++\n").lower()
    if player_command == "start":
        player = Player(name)
        level = 1
        enemy = Enemy(level)
        while True:
            try:
                player.attack(enemy)
                print("-" * 38)
                print("|  Your lives: {}  |  Enemy lives: {}  |".format(player.lives, enemy.lives))
                print("-" * 38)
                player.defence(enemy)
                print("-" * 38)
                print("|  Your lives: {}  |  Enemy lives: {}  |".format(player.lives, enemy.lives))
                print("-" * 38)
            except EnemyDown:
                player.score += 5
                level += 1
                enemy.lives = level
                print("_" * 40)
                print("Wow, you KILLED enemy! Congratulations!\n"
                      "Your SCORE: {}.".format(player.score))
                print("¯" * 40)
                enemy = Enemy(level)
            except GameOver:
                print("_" * 33)
                print("Oo, you DIED.\n"
                      "Your SCORE: {}.".format(player.score))
                print("¯" * 33)
                GameOver.write_score(name, player.score)
                raise GameOver
    elif player_command == "help":
        print("_" * 50)
        print("Allowed commands:", ', '.join(ALLOWED_COMMANDS))
        print("¯" * 50, "\n")
        start_play(name)
    elif player_command == "show scores":
        with open('scores.txt', 'r') as file_score:
            for line in file_score:
                print(line)
        start_play(name)
    elif player_command == "exit":
        sys.exit()


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        pass
    except KeyboardInterrupt:
        pass
    finally:
        print("\n"
              "+++++++++++++++\n"
              "+  Good bye!  +\n"
              "+++++++++++++++\n")
