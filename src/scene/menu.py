from PyQt6.QtWidgets import QPushButton

class Menu:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.button = QPushButton("Play", mainWindow)
        self.button.setGeometry((int)(mainWindow.width / 2) - 100, (int)(mainWindow.height / 2) - 15, 200, 30)

        self.button.clicked.connect(mainWindow.start)

    def show(self):
        self.button.show()
    def hide(self):
        self.button.hide()