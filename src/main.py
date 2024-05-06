import sys
from mainWindow import MainWindow
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()
    return 0

if __name__ == "__main__":
    sys.exit(main())
