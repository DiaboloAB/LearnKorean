from PyQt6.QtWidgets import QPushButton

class ClassicMode:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.choice1 = QPushButton("", mainWindow)
        self.choice1.setGeometry((int)(mainWindow.width / 2) - 100 - 200, (int)(mainWindow.height / 2) + 50, 200, 30)
        self.choice1.clicked.connect(lambda: self.check(self.choice1.text()))
        self.choice2 = QPushButton("", mainWindow)
        self.choice2.setGeometry((int)(mainWindow.width / 2) - 100, (int)(mainWindow.height / 2) + 50, 200, 30)
        self.choice2.clicked.connect(lambda: self.check(self.choice2.text()))
        self.choice3 = QPushButton("", mainWindow)
        self.choice3.setGeometry((int)(mainWindow.width / 2) - 100 + 200, (int)(mainWindow.height / 2) + 50, 200, 30)
        self.choice3.clicked.connect(lambda: self.check(self.choice3.text()))
        self.instruction = "Choose the correct English word."

        self.hide()

    def update(self):
        self.correct = True
        self.choice1.setText(self.mainWindow.choices[0].english)
        self.choice2.setText(self.mainWindow.choices[1].english)
        self.choice3.setText(self.mainWindow.choices[2].english)
        self.choice1.setStyleSheet("background-color: none")
        self.choice2.setStyleSheet("background-color: none")
        self.choice3.setStyleSheet("background-color: none")

    def show(self):
        self.choice1.show()
        self.choice2.show()
        self.choice3.show()
    def hide(self):
        self.choice1.hide()
        self.choice2.hide()
        self.choice3.hide()

    def check(self, choice):
        if choice == self.mainWindow.currentCard.english:
            self.mainWindow.streak += 1
            if self.correct is not True:
                self.mainWindow.streak -= 1
            if self.mainWindow.streak > self.mainWindow.bestStreak:
                self.mainWindow.bestStreak = self.mainWindow.streak
            self.mainWindow.Game.update()
        else:
            self.mainWindow.streak = 0
            if choice == self.choice1.text():
                self.choice1.setStyleSheet("background-color: red")
            elif choice == self.choice2.text():
                self.choice2.setStyleSheet("background-color: red")
            else:
                self.choice3.setStyleSheet("background-color: red")
