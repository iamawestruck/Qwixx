import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class GameBoard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.redButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]
        # self.redButtons = [button.setStyleSheet("background-color : red") for button in self.redButtons]

        self.yellowButtons = [QtWidgets.QPushButton(str(i)) for i in range(2, 13)]
        # self.yellowButtons = [button.setStyleSheet("background-color : yellow") for button in self.yellowButtons]

        self.greenButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]
        # self.greenButtons = [button.setStyleSheet("background-color : green") for button in self.greenButtons]

        self.blueButtons = [QtWidgets.QPushButton(str(i)) for i in range(12, 1, -1)]
        # self.blueButtons = [button.setStyleSheet("background-color : blue") for button in self.blueButtons]

        self.redButtonGroup = QtWidgets.QWidget()
        self.redButtonGroup.layout = QtWidgets.QHBoxLayout(self.redButtonGroup)

        self.yellowButtonGroup = QtWidgets.QWidget()
        self.yellowButtonGroup.layout = QtWidgets.QHBoxLayout(self.yellowButtonGroup)

        self.greenButtonGroup = QtWidgets.QWidget()
        self.greenButtonGroup.layout = QtWidgets.QHBoxLayout(self.greenButtonGroup)

        self.blueButtonGroup = QtWidgets.QWidget()
        self.blueButtonGroup.layout = QtWidgets.QHBoxLayout(self.blueButtonGroup)

        for i in range(0,11):
            self.redButtons[i].setStyleSheet("background-color : red")
            self.yellowButtons[i].setStyleSheet("background-color : yellow")
            self.greenButtons[i].setStyleSheet("background-color : green")
            self.blueButtons[i].setStyleSheet("background-color : blue")

            self.redButtonGroup.layout.addWidget(self.redButtons[i])
            self.yellowButtonGroup.layout.addWidget(self.yellowButtons[i])
            self.greenButtonGroup.layout.addWidget(self.greenButtons[i])
            self.blueButtonGroup.layout.addWidget(self.blueButtons[i])

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
