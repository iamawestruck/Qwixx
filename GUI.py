import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from game import Game

game = None
diceGUI = None
boardsGUI = []


class GameBoard(QtWidgets.QWidget):
    playerNumber = None

    def __init__(self, playerNumber):
        super().__init__()
        self.playerNumber = playerNumber
        self.redButtons = QtWidgets.QButtonGroup(self)
        self.yellowButtons = QtWidgets.QButtonGroup(self)
        self.greenButtons = QtWidgets.QButtonGroup(self)
        self.blueButtons = QtWidgets.QButtonGroup(self)

        self.redButtonGroup = QtWidgets.QWidget()
        self.redButtonGroup.layout = QtWidgets.QHBoxLayout(self.redButtonGroup)

        self.yellowButtonGroup = QtWidgets.QWidget()
        self.yellowButtonGroup.layout = QtWidgets.QHBoxLayout(self.yellowButtonGroup)

        self.greenButtonGroup = QtWidgets.QWidget()
        self.greenButtonGroup.layout = QtWidgets.QHBoxLayout(self.greenButtonGroup)

        self.blueButtonGroup = QtWidgets.QWidget()
        self.blueButtonGroup.layout = QtWidgets.QHBoxLayout(self.blueButtonGroup)

        for i in range(0, 11):
            redButton = QtWidgets.QPushButton(str(i+2))
            redButton.setStyleSheet("background-color : #ff6961")
            self.redButtons.addButton(redButton, i)
            self.redButtonGroup.layout.addWidget(redButton)

            yellowButton = QtWidgets.QPushButton(str(i + 2))
            yellowButton.setStyleSheet("background-color : #fdfd96")
            self.yellowButtons.addButton(yellowButton, i)
            self.yellowButtonGroup.layout.addWidget(yellowButton)

            greenButton = QtWidgets.QPushButton(str(12 - i))
            greenButton.setStyleSheet("background-color : #77dd77")
            self.greenButtons.addButton(greenButton, i)
            self.greenButtonGroup.layout.addWidget(greenButton)

            blueButton = QtWidgets.QPushButton(str(12 - i))
            blueButton.setStyleSheet("background-color : #90d4ed")
            self.blueButtons.addButton(blueButton, i)
            self.blueButtonGroup.layout.addWidget(blueButton)

        self.redButtons.idClicked.connect(lambda i: self.boardNumberedColoredButtonClicked(i+2, "red"))
        self.yellowButtons.idClicked.connect(lambda i: self.boardNumberedColoredButtonClicked(i+2, "yellow"))
        self.greenButtons.idClicked.connect(lambda i: self.boardNumberedColoredButtonClicked(12-i, "green"))
        self.blueButtons.idClicked.connect(lambda i: self.boardNumberedColoredButtonClicked(12-i, "blue"))


        # for i in range(0, 11):
        #     self.redButtons[i].clicked.connect(lambda i = i: self.boardNumberedColoredButtonClicked(
        #         "red", i+2))
        #     self.yellowButtons[i].clicked.connect(lambda: self.boardNumberedColoredButtonClicked(
        #         "yellow", self.yellowButtons[i].text()))
        #     self.greenButtons[i].clicked.connect(lambda: self.boardNumberedColoredButtonClicked(
        #         "green", self.greenButtons[i].text()))
        #     self.blueButtons[i].clicked.connect(lambda: self.boardNumberedColoredButtonClicked(
        #         "blue", self.blueButtons[i].text()))
        #     self.redButtons[i].setStyleSheet("background-color : red")
        #     self.yellowButtons[i].setStyleSheet("background-color : yellow")
        #     self.greenButtons[i].setStyleSheet("background-color : green")
        #     self.blueButtons[i].setStyleSheet("background-color : #0080ff")
        #
        #     self.redButtonGroup.layout.addWidget(self.redButtons[i])
        #     self.yellowButtonGroup.layout.addWidget(self.yellowButtons[i])
        #     self.greenButtonGroup.layout.addWidget(self.greenButtons[i])
        #     self.blueButtonGroup.layout.addWidget(self.blueButtons[i])

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.redButtonGroup)
        self.layout.addWidget(self.yellowButtonGroup)
        self.layout.addWidget(self.greenButtonGroup)
        self.layout.addWidget(self.blueButtonGroup)

    def boardNumberedColoredButtonClicked(self, number, color):
        global game
        game.players[self.playerNumber].setColoredNumber(color, number)
        print(game.players[self.playerNumber].red)
        self.updateGameBoardGUI()

    def updateGameBoardGUI(self):
        board = game.players[self.playerNumber]
        redButtonGroupChildren = self.redButtonGroup.children()
        for value in board.red:
            redButtonGroupChildren[value-1].setStyleSheet("background-color : #660500")
        yellowButtonGroupChildren = self.yellowButtonGroup.children()
        for value in board.yellow:
            yellowButtonGroupChildren[value-1].setStyleSheet("background-color : #646402")
        greenButtonGroupChildren = self.greenButtonGroup.children()
        for value in board.green:
            greenButtonGroupChildren[13-value].setStyleSheet("background-color : #145214")
        blueButtonGroupChildren = self.blueButtonGroup.children()
        for value in board.blue:
            blueButtonGroupChildren[13-value].setStyleSheet("background-color : #0e4458")


class DiceRoll(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        dice = [0, 1, 2, 3, 4, 5]
        self.diceButtons = [QtWidgets.QPushButton(str(dice[i])) for i in range(0, 6)]
        self.rollButton = QtWidgets.QPushButton("Roll")
        self.rollButton.clicked.connect(self.updateDiceGUI)
        self.layout = QtWidgets.QVBoxLayout(self)

        self.upperButtons = QtWidgets.QWidget()
        self.middleButtons = QtWidgets.QWidget()
        self.lowerButtons = QtWidgets.QWidget()
        self.lowestButton = QtWidgets.QWidget()

        self.upperButtons.layout = QtWidgets.QHBoxLayout(self.upperButtons)
        self.middleButtons.layout = QtWidgets.QHBoxLayout(self.middleButtons)
        self.lowerButtons.layout = QtWidgets.QHBoxLayout(self.lowerButtons)
        self.lowestButton.layout = QtWidgets.QHBoxLayout(self.lowestButton)

        self.upperButtons.layout.addWidget(self.diceButtons[0])
        self.upperButtons.layout.addWidget(self.diceButtons[1])

        self.diceButtons[2].setStyleSheet("background-color : #ff6961")
        self.diceButtons[3].setStyleSheet("background-color : #fdfd96")
        self.middleButtons.layout.addWidget(self.diceButtons[2])
        self.middleButtons.layout.addWidget(self.diceButtons[3])

        self.diceButtons[4].setStyleSheet("background-color : #77dd77")
        self.diceButtons[5].setStyleSheet("background-color : #90d4ed")
        self.lowerButtons.layout.addWidget(self.diceButtons[4])
        self.lowerButtons.layout.addWidget(self.diceButtons[5])

        self.lowestButton.layout.addWidget(self.rollButton)

        self.layout.addWidget(self.upperButtons)
        self.layout.addWidget(self.middleButtons)
        self.layout.addWidget(self.lowerButtons)
        self.layout.addWidget(self.lowestButton)

    def updateDiceGUI(self):
        global game
        game.rollDice()
        for i in range(len(self.diceButtons)):
            if self.diceButtons[i] != None:
                self.diceButtons[i].setText(str(game.dice[i]))
            else:
                self.diceButtons[i].setText("")
                self.diceButtons[i].setStyleSheet("background-color: #333333")


def startUp():
    global game, diceGUI, boardsGUI
    game = Game()
    diceGUI = DiceRoll()
    boardsGUI.append(GameBoard(0))
    game.addPlayer()
    diceGUI.show()
    boardsGUI[0].show()
    diceGUI.updateDiceGUI()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    startUp()
    sys.exit(app.exec())

