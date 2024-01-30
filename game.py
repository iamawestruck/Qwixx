from player import Player
import random


class Game:
    playerCount = None
    # dice array order is white1, white2, red, yellow, green, blue
    dice = []

    def getPlayerCount(self):
        self.playerCount = int(input("How many players will be joining? \n"))

    
    def __init__(self):
        self.getPlayerCount()
        print(self.playerCount)

    def rollDice(self):
        self.dice = [random.randint(1, 6) for _ in range(6)]

