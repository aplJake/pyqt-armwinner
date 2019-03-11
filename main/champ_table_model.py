from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from utils import table_style
from helpers.tour_helper import players_linked_list

from helpers.tour_history.history_actions import WrapperAction
from helpers.tour_history.stack import Stack
from helpers.tour_helper.players_linked_list import DoublePlayersPairList, PlayingPair

class EliminationTMDLL:
    playerPairsDLL = None
    currentPairNode = None
    stackHistory = None

    def __init__(self, tableView: QTableView, type=None):
        self.stackHistory = Stack(type)

        # set model for QTableView
        self.tableModel = QStandardItemModel(0, 3)
        self.modelType = type
        self.tableView = tableView 
        # self.name = name
        self.points = 0       

        self.header = ["#", "Имя", "Победитель"]
        self.tableModel.setHorizontalHeaderLabels(self.header)
        tableView.setModel(self.tableModel)
        self.customizeTableViewUI(tableView)
    
    # history stack
    def addHistoryAction(self, action1=None, action2=None, action3=False):
        self.stackHistory.push(WrapperAction(action1, action2, action3))
    
    def realeseHistoryAction(self):
        self.stackHistory.pop()

    
    def getRowCount(self):
        return self.tableModel.rowCount()

    def formPlayingPairs(self):
        names = self.getModelData()

        # partition of array
        partitionedNames = self.__partition(names)
        # form DLL
        self.playerPairsDLL = DoublePlayersPairList()
        for playersPair in partitionedNames:
            self.playerPairsDLL.append(playersPair)
        
        # set initially current node
        self.currentPairNode = self.playerPairsDLL.head 
        return self.playerPairsDLL

    def forPlayingPairsFromTail(self):
        names = self.getModelData()

        # partition of array
        partitionedNames = self.__partition(names)
        # form DLL
        self.playerPairsDLL = DoublePlayersPairList()
        for playersPair in partitionedNames:
            self.playerPairsDLL.append(playersPair)
        
        # set initially current node
        self.currentPairNode = self.playerPairsDLL.tail 
        return self.currentPairNode

    @staticmethod
    def __partition(players):
        def chunks(l, n):
            for i in range(0, len(l), n):
                yield l[i:i + n]

        temp = []
        for pair in list(chunks(players, 2)):
            if len(pair) == 2:
                temp.append(PlayingPair(pair))
            else:
                temp.append(PlayingPair([pair[0], None]))
        return temp
    
    def removeData(self, index):
        self.tableModel.removeRow(index[0].row())
    
    def removeRow(self, row):
        self.tableModel.removeRow(row)
        self.updateView()

    def getModelData(self):
        # TODO: change model
        data = []
        for row in range(self.getRowCount()):
            # data.append([])
            nameIndex = self.tableModel.index(row, 1)
            name = str(self.tableModel.data(nameIndex))
            # We suppose data are strings
            data.append(name)
        return data
    
    def getWinnerModelData(self):
        # TODO: change model
        data = []
        for row in range(self.getRowCount()):
            # data.append([])
            nameIndex = self.tableModel.index(row, 1)
            winnerIndex = self.tableModel.index(row, 2)
            name = str(self.tableModel.data(nameIndex))
            isWinner = str(self.tableModel.data(winnerIndex))
            # We suppose data are strings
            data.append([name, isWinner])
        return data

    def addData(self, data):
        def populateIndex():
            tableIndexToAdd = self.getRowCount()
            lastPairIndex = self.tableModel.data(self.tableModel.index(tableIndexToAdd - 1, 0))
            # if table model is empty then set first pair with index 1
            if lastPairIndex is None:
                self.tableModel.setItem(0, 0, QStandardItem("1"))
            # if is not empty
            else:
                if tableIndexToAdd % 2 == 0:
                    strIndex = str(int(lastPairIndex)+1)
                    self.tableModel.setItem(tableIndexToAdd, 0, QStandardItem(strIndex))
                else:
                    self.tableModel.setItem(tableIndexToAdd, 0, QStandardItem(str(lastPairIndex)))
        # set pair index and item
        populateIndex()
        
        indexItem = self.tableModel.index(self.getRowCount()-1, 1)
        self.tableModel.setItem(self.getRowCount()-1, 1, QStandardItem(str(data)) )
        # update the DLL
        self.formPlayingPairs()
        return indexItem

    def populateIndex(self):
        rows = self.getRowCount()
        counter = 0
        for row in range(rows):
            if row % 2 == 0:
                # strIndex = str(int(lastPairIndex)+1)
                counter += 1
                self.tableModel.setItem(row, 0, QStandardItem(str(counter)))
            else:
                self.tableModel.setItem(row, 0, QStandardItem(str(counter)))

    # setter for winner oclumn in champ tables
    def isWinner(self, row, value, column=2):
        self.tableModel.setItem(row, column, QStandardItem(str(value)))
    
    # push from start of DLL
    def push(self, data):
        # insert an empty row
        self.tableModel.insertRow(0)
        # insert row and update all rows in the table model
        self.tableModel.setItem(0, 0, QStandardItem(str(1)))
        self.populateIndex()
        self.tableModel.setItem(0, 1, QStandardItem(str(data)))
        self.formPlayingPairs()
        return self.tableModel.index(0, 1)

    def updateCurrentPair(self):
        if self.currentPairNode.nextPair is not None:
            self.currentPairNode = self.currentPairNode.nextPair
            return True
        else:
            return False
    
    def popItem(self):
        rowIndex = self.getRowCount()
        if (rowIndex is not None) and (rowIndex >= 1):
            self.tableModel.removeRow(rowIndex - 1)
            self.updateView()
            # self.formPlayingPairs()
            return True
        else:
            return False

    def popFromStart(self):
        self.tableModel.removeRow(0)
        self.updateView()
    
    def updateView(self):
        rows = self.getRowCount()
        data = self.getModelData()
        print("DATA", data)
        self.tableModel.clear()
        # self.tableModel.setRowCount(rows)
        self.tableModel.setHorizontalHeaderLabels(['#', 'Игрок', "Победитель"])
        self.customizeTableViewUI(self.tableView)

        self.addUpdatedData(data)

    def addUpdatedData(self, data):
        for item in data:
            self.addData(item)

    @staticmethod
    def customizeTableViewUI(tableView):
        # set init ui for mainTV
        table_style.setTableDesignW10(tableView)
        tableView.horizontalHeader().resizeSection(0, 18)
