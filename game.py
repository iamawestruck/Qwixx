from player import Player
import random
import time

class Game:
    playerCount = None
    # dice array order is white1, white2, red, yellow, green, blue
    dice = []
    players = []

    # def getPlayerCount(self):
    #     self.playerCount = int(input("How many players will be joining? \n"))

    
    def __init__(self):
        # self.getPlayerCount()
        # print(self.playerCount)
        # This is where
        # we would go through initializations of each game board.
        variable = 2
        self.rollDice()

    def addPlayer(self):
        self.players.append(Player())

    def rollDice(self):
        self.dice = [random.randint(1, 6) for i in range(6) if self.dice is not None]
