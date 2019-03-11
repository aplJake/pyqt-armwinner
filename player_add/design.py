# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_user_adding.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addPlayerQObject(object):
    def setupUi(self, addPlayerQObject):
        addPlayerQObject.setObjectName("addPlayerQObject")
        addPlayerQObject.setEnabled(True)
        addPlayerQObject.resize(248, 305)
        self.addPlayerBtn = QtWidgets.QPushButton(addPlayerQObject)
        self.addPlayerBtn.setGeometry(QtCore.QRect(60, 260, 75, 23))
        self.addPlayerBtn.setObjectName("addPlayerBtn")
        self.cancelAddPlayerBtn = QtWidgets.QPushButton(addPlayerQObject)
        self.cancelAddPlayerBtn.setGeometry(QtCore.QRect(160, 260, 75, 23))
        self.cancelAddPlayerBtn.setObjectName("cancelAddPlayerBtn")
        self.layoutWidget = QtWidgets.QWidget(addPlayerQObject)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 181, 221))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.verticalLayout.addWidget(self.nameLineEdit)
        self.teamLabel = QtWidgets.QLabel(self.layoutWidget)
        self.teamLabel.setObjectName("teamLabel")
        self.verticalLayout.addWidget(self.teamLabel)
        self.teamLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.teamLineEdit.setObjectName("teamLineEdit")
        self.verticalLayout.addWidget(self.teamLineEdit)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.qualLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.qualLineEdit.setObjectName("qualLineEdit")
        self.verticalLayout.addWidget(self.qualLineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.weightLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.weightLineEdit.setText("")
        self.weightLineEdit.setObjectName("weightLineEdit")
        self.verticalLayout.addWidget(self.weightLineEdit)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.idNumberTextEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.idNumberTextEdit.setText("")
        self.idNumberTextEdit.setObjectName("idNumberTextEdit")
        self.verticalLayout.addWidget(self.idNumberTextEdit)

        self.retranslateUi(addPlayerQObject)
        QtCore.QMetaObject.connectSlotsByName(addPlayerQObject)
        addPlayerQObject.setTabOrder(self.nameLineEdit, self.teamLineEdit)
        addPlayerQObject.setTabOrder(self.teamLineEdit, self.qualLineEdit)
        addPlayerQObject.setTabOrder(self.qualLineEdit, self.weightLineEdit)
        addPlayerQObject.setTabOrder(self.weightLineEdit, self.addPlayerBtn)
        addPlayerQObject.setTabOrder(self.addPlayerBtn, self.cancelAddPlayerBtn)

    def retranslateUi(self, addPlayerQObject):
        _translate = QtCore.QCoreApplication.translate
        addPlayerQObject.setWindowTitle(_translate("addPlayerQObject", "Добавить участника"))
        self.addPlayerBtn.setText(_translate("addPlayerQObject", "Добавить"))
        self.cancelAddPlayerBtn.setText(_translate("addPlayerQObject", "Отменить"))
        self.label.setText(_translate("addPlayerQObject", "Имя"))
        self.teamLabel.setText(_translate("addPlayerQObject", "Команда"))
        self.label_4.setText(_translate("addPlayerQObject", "Квалификация"))
        self.label_5.setText(_translate("addPlayerQObject", "Вес"))
        self.label_6.setText(_translate("addPlayerQObject", "Ж номер"))

