from PyQt5.QtWidgets import QMessageBox

def showAlertMsg(title, msg):
    msgBox = QMessageBox()
    msgBox.setWindowTitle(str(title))
    msgBox.setText(str(msg))
    msgBox.exec_()