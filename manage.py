from main.app import Main
from PyQt5.QtWidgets import QApplication
import sys

def Start():
    m = Main()
    m.show()
    return m
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    wndow = Start()
    app.exec_()