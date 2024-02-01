import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from game import Game

game = None
diceGUI = None
boardsGUI = []

class GameBoard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.redButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]

        self.yellowButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]

        self.greenButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]

        self.blueButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]

        self.redButtonGroup = QtWidgets.QWidget()
        self.redButtonGroup.layout = QtWidgets.QHBoxLayout(self.redButtonGroup)

        self.yellowButtonGroup = QtWidgets.QWidget()
        self.yellowButtonGroup.layout = QtWidgets.QHBoxLayout(self.yellowButtonGroup)

        self.greenButtonGroup = QtWidgets.QWidget()
        self.greenButtonGroup.layout = QtWidgets.QHBoxLayout(self.greenButtonGroup)

        self.blueButtonGroup = QtWidgets.QWidget()
        self.blueButtonGroup.layout = QtWidgets.QHBoxLayout(self.blueButtonGroup)

        for i in range(0, 11):
            self.redButtons[i].setStyleSheet("background-color : red")
            self.yellowButtons[i].setStyleSheet("background-color : yellow")
            self.greenButtons[i].setStyleSheet("background-color : green")
            self.blueButtons[i].setStyleSheet("background-color : #0080ff")

            self.redButtonGroup.layout.addWidget(self.redButtons[i])
            self.yellowButtonGroup.layout.addWidget(self.yellowButtons[i])
            self.greenButtonGroup.layout.addWidget(self.greenButtons[i])
            self.blueButtonGroup.layout.addWidget(self.blueButtons[i])

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.redButtonGroup)
        self.layout.addWidget(self.yellowButtonGroup)
        self.layout.addWidget(self.greenButtonGroup)
        self.layout.addWidget(self.blueButtonGroup)


class DiceRoll(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        dice = [0, 1, 2, 3, 4, 5]
        self.diceButtons = [QtWidgets.QPushButton(str(dice[i])) for i in range(0, 6)]
        self.rollButton = QtWidgets.QPushButton("Roll")
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

        self.diceButtons[2].setStyleSheet("background-color : red")
        self.diceButtons[3].setStyleSheet("background-color : yellow")
        self.middleButtons.layout.addWidget(self.diceButtons[2])
        self.middleButtons.layout.addWidget(self.diceButtons[3])

        self.diceButtons[4].setStyleSheet("background-color : green")
        self.diceButtons[5].setStyleSheet("background-color : #0080ff")
        self.lowerButtons.layout.addWidget(self.diceButtons[4])
        self.lowerButtons.layout.addWidget(self.diceButtons[5])

        self.lowestButton.layout.addWidget(self.rollButton)

        self.layout.addWidget(self.upperButtons)
        self.layout.addWidget(self.middleButtons)
        self.layout.addWidget(self.lowerButtons)
        self.layout.addWidget(self.lowestButton)

    def updateDiceGUI(self, values):
        for i in range(len(self.diceButtons)):
            self.diceButtons[i].setText(str(values[i]))


def startUp():
    global game, diceGUI, boardsGUI
    game = Game()
    diceGUI = DiceRoll()
    boardsGUI.append(GameBoard())
    diceGUI.show()
    boardsGUI[0].show()
    diceGUI.updateDiceGUI(game.dice)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    startUp()
    sys.exit(app.exec())

