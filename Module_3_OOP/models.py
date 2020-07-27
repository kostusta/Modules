"""
A module that describes player classes
"""
from random import randint

from exceptions import GameOver, EnemyDown
from settings import DEF_LIVES_COUNT
from settings import ALLOWED_DRAFTS


class Enemy:
    """
    Class that describes the adversary
    """

    def __init__(self, level):
        """
        Init function
        :param level: level
        """
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        The function that helps to choose an attack
        :return: random number in range 1 - 3
        """
        return randint(1, 3)

    def decrease_lives(self,):
        """
        The function that decrease a number of game character lives
        :return: None
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player:
    """
    A class that describes your game hero
    """

    def __init__(self, name):
        """
        Init function
        :param name: name
        """
        self.name = name
        self.lives = DEF_LIVES_COUNT
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        A function that returns the result of the round - 0 if the draw,
         -1 if the attack is unsuccessful, 1 if the attack is successful
        :return: 0, 1, -1
        """
        if attack == defense:
            return 0
        if attack == 1:
            if defense == 2:
                return 1
        if attack == 2:
            if defense == 3:
                return 1
        if attack == 3:
            if defense == 1:
                return 1
        else:
            return -1

    def decrease_lives(self):
        """
        A function that decrease lives of game hero and raises a GameOver exception
        :return: None
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        """
        A function that receives input from the user (1, 2, 3),
        selects the enemy attack from the enemy_obj object;
        calls the fight () method;
        If the result of the battle is 0, print "It's a draw!", If 1 = 'You attacked successfully!'
        :return: None
        """
        attacks = None
        while attacks not in ALLOWED_DRAFTS:
            try:
                attacks = int(input("Select Attack to User: "
                                    "1 -> WIZARD, "
                                    "2 -> WARRIOR, "
                                    "3 -> ROGUE:\n"))
                if attacks not in ALLOWED_DRAFTS:
                    raise ValueError
            except ValueError:
                print("Wrong input! Try again.")
        enemy_defence = enemy_obj.select_attack()
        res = self.fight(attacks, enemy_defence)
        if res == 0:
            print("It\'s a draw!")
        elif res == 1:
            print("You attacked successfully!")
            self.score += 1
            enemy_obj.decrease_lives()
        else:
            print("You missed!")

    def defence(self, enemy_obj):
        """
        A function that the same as the 'attack'method,
        but the opponent’s attack is transferred to the fight method first,
        and if the opponent’s attack is successful, the player’s decrease_lives method is called
        :return: None
        """
        defense = None
        while defense not in ALLOWED_DRAFTS:
            try:
                defense = int(input("Select Defense to User: "
                                    "1 -> WIZARD, "
                                    "2 -> WARRIOR, "
                                    "3 -> ROGUE:\n"))
                if defense not in ALLOWED_DRAFTS:
                    raise ValueError
            except ValueError:
                print("Wrong input! Try again.")
        enemy_attack = enemy_obj.select_attack()
        res = self.fight(enemy_attack, defense)
        if res == 0:
            print("It\'s a draw!")
        elif res == -1:
            print("You defence successfully!")
        elif res == 1:
            print("You missed!")
            self.decrease_lives()
