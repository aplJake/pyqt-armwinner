# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_playing_pair.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Fighting(object):
    def setupUi(self, Fighting):
        Fighting.setObjectName("Fighting")
        Fighting.resize(230, 280)
        self.groupBox = QtWidgets.QGroupBox(Fighting)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 211, 151))
        self.groupBox.setObjectName("groupBox")
        self.wonFirstPlayerBtn = QtWidgets.QPushButton(self.groupBox)
        self.wonFirstPlayerBtn.setGeometry(QtCore.QRect(70, 10, 75, 23))
        self.wonFirstPlayerBtn.setObjectName("wonFirstPlayerBtn")
        self.wonSecondPlayerBtn = QtWidgets.QPushButton(self.groupBox)
        self.wonSecondPlayerBtn.setGeometry(QtCore.QRect(70, 120, 75, 23))
        self.wonSecondPlayerBtn.setObjectName("wonSecondPlayerBtn")
        self.pairTableView = QtWidgets.QTableView(self.groupBox)
        self.pairTableView.setGeometry(QtCore.QRect(10, 40, 191, 71))
        self.pairTableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pairTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pairTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pairTableView.setObjectName("pairTableView")
        self.pairTableView.horizontalHeader().setVisible(False)
        self.pairTableView.horizontalHeader().setStretchLastSection(True)
        self.pairTableView.verticalHeader().setVisible(False)
        self.pairTableView.verticalHeader().setDefaultSectionSize(35)
        self.groupBox_3 = QtWidgets.QGroupBox(Fighting)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 0, 211, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 191, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.currentTourLabel = QtWidgets.QLabel(self.layoutWidget)
        self.currentTourLabel.setObjectName("currentTourLabel")
        self.horizontalLayout_2.addWidget(self.currentTourLabel)
        self.backTourBtn = QtWidgets.QPushButton(Fighting)
        self.backTourBtn.setGeometry(QtCore.QRect(20, 230, 75, 23))
        self.backTourBtn.setObjectName("backTourBtn")
        self.nextTourBtn = QtWidgets.QPushButton(Fighting)
        self.nextTourBtn.setEnabled(False)
        self.nextTourBtn.setGeometry(QtCore.QRect(120, 230, 75, 23))
        self.nextTourBtn.setObjectName("nextTourBtn")

        self.retranslateUi(Fighting)
        QtCore.QMetaObject.connectSlotsByName(Fighting)

    def retranslateUi(self, Fighting):
        _translate = QtCore.QCoreApplication.translate
        Fighting.setWindowTitle(_translate("Fighting", "Dialog"))
        self.groupBox.setTitle(_translate("Fighting", "Борются"))
        self.wonFirstPlayerBtn.setText(_translate("Fighting", "Победил"))
        self.wonSecondPlayerBtn.setText(_translate("Fighting", "Победил"))
        self.groupBox_3.setTitle(_translate("Fighting", "Информация"))
        self.label.setText(_translate("Fighting", "Название тура"))
        self.currentTourLabel.setText(_translate("Fighting", "Тур 1"))
        self.backTourBtn.setText(_translate("Fighting", "Назад"))
        self.nextTourBtn.setText(_translate("Fighting", "Вперед"))

