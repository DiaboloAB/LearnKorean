from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from definitions import bold, normal
from scene.gameMode.classic import ClassicMode
from scene.gameMode.rewrite import RewriteMode

class Streak:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.label = QLabel("", mainWindow)
        self.label.setFont(normal)
        self.label.setGeometry(0, 0, mainWindow.width, 30)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hide()

    def update(self):
        str = ""
        for i in range(self.mainWindow.streak):
            str += "🔥"
        self.label.setText(str)

    def show(self):
        self.label.show()
    def hide(self):
        self.label.hide()

class Instruction:
    def __init__(self, mainWindow):
        self.label = QLabel("", mainWindow)
        self.label.setFont(normal)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setGeometry(0, (int)(mainWindow.height / 2) - 75, mainWindow.width, 30)
        self.hide()

    def setText(self, text):
        self.label.setText(text)

    def show(self):
        self.label.show()
    def hide(self):
        self.label.hide()

class Korean:
    def __init__(self, mainWindow):
        self.label = QLabel("", mainWindow)
        self.label.setFont(bold)
        self.label.setGeometry((int)(mainWindow.width / 2) - 250, (int)(mainWindow.height / 2) - 25, 500, 50)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hide()

    def setText(self, text):
        self.label.setText(text)

    def show(self):
        self.label.show()
    def hide(self):
        self.label.hide()

class Game:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.instructions = Instruction(mainWindow)
        self.korean = Korean(mainWindow)
        self.streak = Streak(mainWindow)

        self.modes = [ClassicMode(self.mainWindow), RewriteMode(self.mainWindow)]
        self.currentMode = 0

        self.hide()

    def show(self):
        self.instructions.show()
        self.korean.show()
        self.streak.show()
    def hide(self):
        self.instructions.hide()
        self.korean.hide()
        self.streak.hide()

    def changeMode(self):
        self.modes[self.currentMode].hide()
        self.currentMode = (self.currentMode + 1) % len(self.modes)
        self.modes[self.currentMode].show()

    def update(self):
        self.mainWindow.newCard()
        self.korean.setText(self.mainWindow.currentCard.korean)
        self.streak.update()
        self.changeMode()
        self.modes[self.currentMode].update()
        self.instructions.setText(self.modes[self.currentMode].instruction)
