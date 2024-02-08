import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from game import Game

game = None
diceGUI = None
boardsGUI = []
playerNumberGUI = None


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
        self.submitButton = QtWidgets.QPushButton("Submit")
        self.submitButton.clicked.connect(self.submitButtonClicked)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.redButtonGroup)
        self.layout.addWidget(self.yellowButtonGroup)
        self.layout.addWidget(self.greenButtonGroup)
        self.layout.addWidget(self.blueButtonGroup)
        self.layout.addWidget(self.submitButton)
        self.setWindowTitle(f"Player {playerNumber+1}")

    def submitButtonClicked(self):
        global game, boardsGUI
        if game.activeTurn.isActive:
            if game.activeTurn.checkMove(game.players[self.playerNumber]):
                if game.activeTurn.hasAMove():
                    game.activePlayerMadeMove = True
                game.activeTurn.addToPlayerBoard(game.players[self.playerNumber])
                self.updateGameBoardGUI()
                game.newTurn(False)
            else:
                game.newTurn()
        else:
            if game.activeTurn.checkMove(game.players[self.playerNumber]):
                if game.activeTurn.hasAMove():
                    game.activePlayerMadeMove = True
                else:
                    if game.playerWithPriority == game.activePlayer and not game.activePlayerMadeMove:

                        game.players[game.activePlayer].penalty += 5
                game.activeTurn.addToPlayerBoard(game.players[self.playerNumber])
                self.updateGameBoardGUI()
                game.playerWithPriority = (game.playerWithPriority + 1) % len(game.players)
                game.newTurn(False)
                if game.playerWithPriority == game.activePlayer:
                    self.setDisabled(True)
                    nextTurn()
                else:
                    boardsGUI[game.playerWithPriority].setEnabled(True)
                    self.setDisabled(True)
            else:
                game.newTurn(False)




    def boardNumberedColoredButtonClicked(self, number, color):
        global game
        game.activeTurn.addToMove(color, number)


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


class PlayerCountPopUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("How many players will be joining?",
                                     alignment=QtCore.Qt.AlignCenter)

        self.button1 = QtWidgets.QPushButton("2 Players")
        self.button2 = QtWidgets.QPushButton("3 Players")
        self.button3 = QtWidgets.QPushButton("4 Players")
        self.button4 = QtWidgets.QPushButton("5 Players")

        self.button1.clicked.connect(lambda: self.startGame(2))
        self.button2.clicked.connect(lambda: self.startGame(3))
        self.button3.clicked.connect(lambda: self.startGame(4))
        self.button4.clicked.connect(lambda: self.startGame(5))

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

        self.upperButtons = QtWidgets.QWidget()
        self.lowerButtons = QtWidgets.QWidget()
        self.upperButtons.layout = QtWidgets.QHBoxLayout(self.upperButtons)
        self.lowerButtons.layout = QtWidgets.QHBoxLayout(self.lowerButtons)
        self.upperButtons.layout.addWidget(self.button1)
        self.upperButtons.layout.addWidget(self.button2)
        self.lowerButtons.layout.addWidget(self.button3)
        self.lowerButtons.layout.addWidget(self.button4)

        self.layout.addWidget(self.upperButtons)
        self.layout.addWidget(self.lowerButtons)

    def startGame(self, playerCount):
        global game, boardsGUI, diceGUI
        for i in range(playerCount):
            boardsGUI.append(GameBoard(i))
            boardsGUI[i].show()
            game.addPlayer()
        game.activePlayer = random.randint(0, playerCount-1)
        game.playerWithPriority = game.activePlayer
        game.activePlayerMadeSecondMove = False
        setActivePlayer()
        diceGUI.show()
        diceGUI.updateDiceGUI()
        diceGUI.setDisabled(True)
        game.newTurn()
        self.hide()


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
            print(self.diceButtons)
            if game.dice[i] != None:
                self.diceButtons[i].setText(str(game.dice[i]))
            else:
                self.diceButtons[i].setText("")
                self.diceButtons[i].setStyleSheet("background-color: #333333")
        setActivePlayer()
        self.setDisabled(True)



def startUp():
    global game, diceGUI, boardsGUI, playerNumberGUI
    game = Game()
    diceGUI = DiceRoll()
    playerNumberGUI = PlayerCountPopUp()
    playerNumberGUI.show()

# def rotateTurnWithoutDiceRoll():
#     # gotta restructure this to work asynchronously (with slots)
#     global game, boardsGUI
#     previousActivePlayer = game.activePlayer
#     currentActivePlayer = len(game.players) % (game.activePlayer + 1)
#     while currentActivePlayer != game.activePlayer:
#         boardsGUI[previousActivePlayer].setDisabled(True)
#         boardsGUI[currentActivePlayer].setEnabled(True)
#         game.activeTurn = game.Turn(game.dice, False)
#         previousActivePlayer = currentActivePlayer
#         currentActivePlayer = len(game.players) % (game.activePlayer + 1)
def nextTurn():
    checkForLockedRows()
    if gameEnded():
        calculateFinalScore()
    game.activePlayer = (game.activePlayer + 1) % len(game.players)
    game.playerWithPriority = game.activePlayer
    game.activePlayerMadeMove = False
    diceGUI.setEnabled(True)
    game.newTurn()

def checkForLockedRows():
    for player in game.players:
        if 12 in player.red:
            game.dice[2] = None
        if 12 in player.yellow:
            game.dice[3] = None
        if 2 in player.green:
            game.dice[4] = None
        if 2 in player.blue:
            game.dice[5] = None
def gameEnded():
    global game
    count = 0
    for i in range(2, 6):
        if game.dice[i] is None:
            count += 1
    if count >= 2:
        return True
    for player in game.players:
        if player.penalty >= 20:
            return True
    return False

def calculateFinalScore():
    global game
    topScoringPlayer = game.players[0]
    topScoringPlayerNum = 1
    playerNum = 1
    for player in game.players:
        player.finalScore += game.scoreDictionary[len(player.red)]
        player.finalScore += game.scoreDictionary[len(player.yellow)]
        player.finalScore += game.scoreDictionary[len(player.green)]
        player.finalScore += game.scoreDictionary[len(player.blue)]
        player.finalScore -= player.penalty
        if player.finalScore > topScoringPlayer.finalScore:
            topScoringPlayer = player
            topScoringPlayerNum = playerNum
        playerNum += 1
    messageBox = QtWidgets.QMessageBox()
    messageBox.setText(f"Player {topScoringPlayerNum} Wins! Final Score: {topScoringPlayer.finalScore}")
    messageBox.buttonClicked.connect(endGame)
    messageBox.exec()

def endGame():
    app.exit()

def setActivePlayer():
    global game, boardsGUI

    for i in range(len(boardsGUI)):
        if i != game.activePlayer:
            boardsGUI[i].setDisabled(True)
        else:
            boardsGUI[i].setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    startUp()
    sys.exit(app.exec())

