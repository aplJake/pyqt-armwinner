from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QMessageBox
from utils import table_style
from helpers.report import json_report

class MainPlayersTM:
    def __init__(self, tableView=None, rows=0, columns=6):
        self.tableModel = QStandardItemModel(rows, columns)

        header = ['Участник', 'Квал.', 'Команда', 'Вес', '# Ж/р', 'Место']
        self.tableModel.setHorizontalHeaderLabels(header)
        self.tableView = tableView
        if tableView is not None:
            self.customizeTableViewUI(tableView)
    
    @property
    def tableModel(self):
        return self.__tableModel

    @tableModel.setter
    def tableModel(self, model):
        self.__tableModel = model
    
    def getRowCount(self):
        return self.tableModel.rowCount()

    def getModelData(self):
        data = []
        for row in range(self.getRowCount()):
            data.append([])
            for column in range(self.tableModel.columnCount()):
                index = self.tableModel.index(row, column)
                # We suppose data are strings
                data[row].append(str(self.tableModel.data(index)))
        return data
    
    def addData(self, data):
        rowToInsert = self.getRowCount()

        for column, key in enumerate(data.__dict__):
            newitem = QStandardItem(data.__dict__[key])
            self.tableModel.setItem(rowToInsert, column, newitem)
    
    def addDataDict(self, data):
        rowToInsert = self.getRowCount()

        for column, key in enumerate(data):
            newitem = QStandardItem(data[key])
            self.tableModel.setItem(rowToInsert, column, newitem)

    def removeData(self, index):
        self.tableModel.removeRow(index[0].row())

    def colorItem(self, row, column, color=QColor(223, 223, 223)):
        self.tableModel.item(row, column).setBackground(color)
    
    def sort(self):
        jsonWriter = json_report.WriteJSON()
        json = jsonWriter.saveMainTM(modelData=self.getModelData())

        try:
            sortedJSON = sorted(json["player_long"], key=lambda x: int(x["номер"]), reverse=False)
            # clear the model and populate empty model 
            self.updateView()

            for row in sortedJSON:
                self.addDataDict(row)
        except IndexError:
            self.showAlertMsg("Ошибка", "Index error wjile sorting json file")
    
    def sortByScore(self, json):
        jsonWriter = json_report.WriteJSON()
        json = jsonWriter.saveMainTM(modelData=self.getModelData())

        try:
            sortedJSON = sorted(json["player_long"], key=lambda x: int(x["номер"]), reverse=True)
            # clear the model and populate empty model 
            self.updateView()

            for row in sortedJSON:
                self.addDataDict(row)
        except IndexError:
            self.showAlertMsg("Ошибка", "Index error wjile sorting json file")

    def updateView(self):
        rows = self.getRowCount()
        data = self.getModelData()
        print("DATA", data)
        self.tableModel.clear()
        # self.tableModel.setRowCount(rows)
        header = ['Участник', 'Квал.', 'Команда', 'Вес', '# Ж/р', 'Место']

        self.tableModel.setHorizontalHeaderLabels(header)
        self.customizeTableViewUI(self.tableView)

    @staticmethod
    def showAlertMsg(title, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(str(title))
        msgBox.setText(str(msg))
        msgBox.exec_()

    @staticmethod
    def customizeTableViewUI(tableView):
        # set init ui for mainTV
        table_style.setTableDesignW10(tableView)
        tableView.horizontalHeader().resizeSection(0, 160)
        tableView.horizontalHeader().resizeSection(1, 10)
        tableView.horizontalHeader().resizeSection(2, 50)
        tableView.horizontalHeader().resizeSection(3, 10)
        tableView.horizontalHeader().resizeSection(4, 15)
        tableView.horizontalHeader().resizeSection(5, 10)
        # sorting indicator by the score column
        # tableView.horizontalHeader().setSortIndicator(4, Qt.DescendingOrder)

        tableView.horizontalHeader().setSortIndicator(5, Qt.DescendingOrder)
