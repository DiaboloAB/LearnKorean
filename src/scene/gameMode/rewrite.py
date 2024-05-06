from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel
from PyQt6.QtGui import QPixmap

class RewriteMode:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.input = QLineEdit(mainWindow)
        self.input.setGeometry((int)(mainWindow.width / 2) - 100, (int)(mainWindow.height / 2) +50, 200, 30)
        self.input.returnPressed.connect(lambda: self.check(self.input.text()))
        self.instruction = "Type the word in Korean."

        self.keyboardImage = QLabel(mainWindow)
        self.keyboardImage.setGeometry((int)(mainWindow.width / 2) - 369, (int)(mainWindow.height / 2) + 90, 737, 200)
        self.keyboardImage.setPixmap(QPixmap("assets/keyboard.jpg"))

        self.hide()

    def update(self):
        self.input.clear()
        self.input.setFocus()

    def show(self):
        self.input.show()
        self.keyboardImage.show()
    def hide(self):
        self.input.hide()
        self.keyboardImage.hide()

    def check(self, choice):
        if choice == self.mainWindow.currentCard.korean:
            self.mainWindow.streak += 1
            if self.mainWindow.streak > self.mainWindow.bestStreak:
                self.mainWindow.bestStreak = self.mainWindow.streak
            self.mainWindow.Game.update()
        else:
            self.mainWindow.streak = 0
            self.mainWindow.Game.update()
