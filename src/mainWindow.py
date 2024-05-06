from PyQt6.QtCore import QByteArray
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QFont

from scene.menu import Menu
from scene.game import Game
from sololingo.sololingo import Sololingo
from definitions import bold, normal

class MainWindow(QMainWindow, Sololingo):
    def __init__(self):
        super().__init__()
        self.height = 600
        self.width = 800
        self.initWindow()
        self.menu = Menu(self)
        self.Game = Game(self)

    def initWindow(self):
        self.setWindowTitle("Sololingo")
        self.setGeometry((int)(1920 / 2 - 400), (int)(1080 / 2 - 200), self.width, self.height)
        self.setFixedSize(800, 600)

    def start(self):
        self.menu.hide()
        self.Game.show()
        self.Game.update()
