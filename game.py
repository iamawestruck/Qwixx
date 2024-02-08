from player import Player
import random
import time

class Game:
    activePlayer = None
    playerWithPriority = None
    # dice array order is white1, white2, red, yellow, green, blue
    dice = None
    players = []
    activeTurn = None
    colorsLocked = []
    activePlayerMadeMove = False
    scoreDictionary = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78]
    # color order is red, yellow, green, blue
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

    def newTurn(self, isActive=True):
        self.activeTurn = Turn(self.dice, isActive)




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

    def hasAMove(self):
        if len(self.red) > 0:
            return True
        if len(self.yellow) > 0:
            return True
        if len(self.green) > 0:
            return True
        if len(self.blue) > 0:
            return True
        return False


    def checkMove(self, player):
        combinedList = []
        combinedList.extend(self.red)
        combinedList.extend(self.yellow)
        combinedList.extend(self.green)
        combinedList.extend(self.blue)
        if len(combinedList) > 1:
            return False
        for i in self.red:
            if not self.diceAddToNumber("red", i):
                return False
            if not player.verifyColoredNumber("red", i):
                return False
        for i in self.yellow:
            if not self.diceAddToNumber("yellow", i):
                return False
            if not player.verifyColoredNumber("yellow", i):
                return False
        for i in self.green:
            if not self.diceAddToNumber("green", i):
                return False
            if not player.verifyColoredNumber("green", i):
                return False
        for i in self.blue:
            if not self.diceAddToNumber("blue", i):
                return False
            if not player.verifyColoredNumber("blue", i):
                return False
        return True

    def diceAddToNumber(self, color, number):
        if self.isActive:
            match color:
                case "red":
                    return self.dice[0] + self.dice[2] == number or self.dice[1] + self.dice[2] == number
                case "yellow":
                    return self.dice[0] + self.dice[3] == number or self.dice[1] + self.dice[3] == number
                case "green":
                    return self.dice[0] + self.dice[4] == number or self.dice[1] + self.dice[4] == number
                case "blue":
                    return self.dice[0] + self.dice[5] == number or self.dice[1] + self.dice[5] == number
        else:
            return self.dice[0] + self.dice[1] == number


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






