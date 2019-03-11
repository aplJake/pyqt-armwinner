from PyQt5.QtGui import QStandardItemModel, QStandardItem
from utils import table_style
class PlayingPairTM:
    def __init__(self, tableView: QStandardItemModel, rows=1, columns=0):
        self.tableModel = QStandardItemModel(rows, columns)
        self.tableView = tableView
        table_style.setTableDesignW10(tableView)

        # partition of player in the model
        self.firstPlayer = None
        self.secondPlayer = None

    def updateTableData(self, data: list):
        # update players information
        self.firstPlayer = str(data[0])
        self.secondPlayer = str(data[1])
        # update table model view
        self.tableModel.setItem(0, 0, QStandardItem(self.firstPlayer))
        self.tableModel.setItem(1, 0, QStandardItem(self.secondPlayer))

    # getters for class attributes #
    def getTableModel(self):
        return self.tableModel

    def getFirstPlayer(self):
        return self.firstPlayer

    def getSecondPlayer(self):
        return self.secondPlayer