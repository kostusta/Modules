"""
Module includes all exceptions for control process of game.
"""
from datetime import datetime


class GameOver(Exception):
    """
    This exception will be called when the player runs out of life.
    """

    @staticmethod
    def write_score(name, score):
        """
        This function writes the result to a file.
        :param name: Player name
        :param score: Player score - final result of game
        :return: writes the result to a file called "scores.txt'
        """
        game_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        with open(r'scores.txt', 'a') as file_score:
            string = "{} : {} | {}\n".format(name, score, game_time)
            return file_score.write(string)


class EnemyDown(Exception):
    """
    This exception will be called when the enemy is killed.
    """
