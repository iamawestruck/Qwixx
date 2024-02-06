from player import Player
import random
import time

class Game:
    activePlayer = None
    # dice array order is white1, white2, red, yellow, green, blue
    dice = None
    players = []
    activeTurn = None
    # def getPlayerCount(self):
    #     self.playerCount = int(input("How many players will be joining? \n"))

    
    def __init__(self):
        # self.getPlayerCount()
        # print(self.playerCount)
        # This is where
        # we would go through initializations of each game board.
        variable = 2
        self.dice = [0, 0, 0, 0, 0, 0]
        self.rollDice()

    def addPlayer(self):
        self.players.append(Player())

    def rollDice(self):
        self.dice = [random.randint(1, 6) for i in range(6) if self.dice[i] is not None]

    def newTurn(self):
        self.activeTurn = Turn(self.dice, True)




class Turn:
    isActive = None
    numMoves = None
    dice = None
    red = None
    yellow = None
    green = None
    blue = None
    # penalty = None

    def __init__(self, dice, isActivePlayer):
        self.isActive = isActivePlayer
        self.numMoves = 0
        self.dice = dice
        self.red = []
        self.yellow = []
        self.green = []
        self.blue = []

    def checkMove(self, player):
        print("checking move")
        for i in self.red:
            if not player.verifyColoredNumber("red", i):
                return False
        for i in self.yellow:
            if not player.verifyColoredNumber("yellow", i):
                return False
        for i in self.green:
            if not player.verifyColoredNumber("green", i):
                return False
        for i in self.blue:
            if not player.verifyColoredNumber("blue", i):
                return False

        return True

    def addToPlayerBoard(self, player):
        self.red.sort()
        self.yellow.sort()
        self.green.sort(reverse=True)
        self.blue.sort(reverse=True)

        player.red.extend(self.red)
        player.yellow.extend(self.yellow)
        player.green.extend(self.green)
        player.blue.extend(self.blue)


    def addToMove(self, color, number):
        match color:
            case "red":
                if number not in self.red:
                    self.red.append(number)
                    self.numMoves += 1
            case "yellow":
                if number not in self.yellow:
                    self.yellow.append(number)
                    self.numMoves += 1
            case "green":
                if number not in self.green:
                    self.green.append(number)
                    self.numMoves += 1
            case "blue":
                if number not in self.blue:
                    self.blue.append(number)
                    self.numMoves += 1






