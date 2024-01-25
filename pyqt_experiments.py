import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class PlayerCountPopUp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text = QtWidgets.QLabel("How many players will be joining?",
                                     alignment=QtCore.Qt.AlignCenter)

        self.button1 = QtWidgets.QPushButton("2 Players")
        self.button2 = QtWidgets.QPushButton("3 Players")
        self.button3 = QtWidgets.QPushButton("4 Players")
        self.button4 = QtWidgets.QPushButton("5 Players")

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

        # @QtCore.Slot()
        # def magic(self):
        #     self.text.setText(random.choice(self.hello))

app = QtWidgets.QApplication([])

widget = PlayerCountPopUp()
widget.resize(800, 600)
widget.show()

sys.exit(app.exec())