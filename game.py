from player import Player
import random
from GUI import *


class Game:
    playerCount = None
    # dice array order is white1, white2, red, yellow, green, blue
    dice = []
    diceGUI = None
    boardsGUI = []

    # def getPlayerCount(self):
    #     self.playerCount = int(input("How many players will be joining? \n"))

    
    def __init__(self):
        # self.getPlayerCount()
        # print(self.playerCount)
        # This is where
        # we would go through initializations of each game board.
        variable = 2
        app = QtWidgets.QApplication([])

        self.boardsGUI.append(GameBoard())
        self.boardsGUI[0].resize(800, 600)
        self.boardsGUI[0].show()
        self.diceGUI = DiceRoll()

        sys.exit(app.exec())




    def rollDice(self):
        self.dice = [random.randint(1, 6) for _ in range(6)]
        self.diceGUI.updateDice(self.dice)





game = Game()
