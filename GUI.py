import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class GameBoard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()



        redButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]
        redButtons = [button.setStyleSheet("background-color : red") for button in redButtons]

        yellowButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]
        yellowButtons = [button.setStyleSheet("background-color : yellow") for button in yellowButtons]

        greenButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]
        greenButtons = [button.setStyleSheet("background-color : green") for button in greenButtons]

        blueButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]
        blueButtons = [button.setStyleSheet("background-color : blue") for button in blueButtons]

        self.redButtonGroup = QtWidgets.QWidget()
        self.redButtonGroup.layout = QtWidgets.QHBoxLayout(self.redButtonGroup)

        self.yellowButtonGroup = QtWidgets.QWidget()
        self.yellowButtonGroup.layout = QtWidgets.QHBoxLayout(self.yellowButtonGroup)

        self.greenButtonGroup = QtWidgets.QWidget()
        self.greenButtonGroup.layout = QtWidgets.QHBoxLayout(self.greenButtonGroup)

        self.blueButtonGroup = QtWidgets.QWidget()
        self.blueButtonGroup.layout = QtWidgets.QHBoxLayout(self.blueButtonGroup)

        for i in range(0,12):
            self.redButtonGroup.layout.addWidget(redButtons[i])
            self.yellowButtonGroup.layout.addWidget(yellowButtons[i])
            self.greenButtonGroup.layout.addWidget(greenButtons[i])
            self.blueButtonGroup.layout.addWidget(blueButtons[i])

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.redButtonGroup)
        self.layout.addWidget(self.yellowButtonGroup)
        self.layout.addWidget(self.greenButtonGroup)
        self.layout.addWidget(self.blueButtonGroup)

app = QtWidgets.QApplication([])

widget = GameBoard()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())
