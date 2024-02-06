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
        self.dice = [random.randint(1, 6) for _ in range(6)]


class Turn:
    isActive = None
    numMoves = None
    red = None
    yellow = None
    green = None
    blue = None
    # penalty = None

    def __init__(self):
        self.numMoves = 0
        self.red = []
        self.yellow = []
        self.green = []
        self.blue = []

    def checkMove(self, player):
        isValid = True
        for i in self.red:
            isValid = isValid & player.verifyColoredNumber("red", i)
        for i in self.yellow:
            isValid = isValid & player.verifyColoredNumber("yellow", i)
        for i in self.green:
            isValid = isValid & player.verifyColoredNumber("green", i)
        for i in self.blue:
            isValid = isValid & player.verifyColoredNumber("blue", i)

        return isValid & self.numMoves < 2






