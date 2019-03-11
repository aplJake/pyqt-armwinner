#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os, datetime
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QStandardItem, QColor

from .design import Ui_MainWindow
from player_add.app import PlayerAdd
from playing_pair.app import PlayingPair
from .main_table_model import MainPlayersTM
from .champ_table_model import EliminationTMDLL
from helpers.report import json_report
from helpers.report import json_to_html
from helpers.enums.champ_model_types import ModelTypes
# from table_models import MainPlayersTM, EliminationTMDLL

# from jsontohtml import JsonToHtml

# for excel report 
# import helper
# from buffer_linked_list import EliminationModel, ModelTypes
class Main(QMainWindow, Ui_MainWindow):
    
    champDialog = None


    def __init__(self):
        super().__init__()
        self.initUI()
        self.setLicence()
    
    def setLicence(self):
        startTrial = datetime.datetime(2019, 3, 1)
        endTrial = datetime.datetime(2019, 6, 23)

        currentDate = datetime.datetime.now()
        if currentDate < endTrial:
            self.setCore()
            self.statusBar().showMessage("Licence trial {}".format(endTrial.date()))
        else:
            self.statusBar().showMessage("Licence trial is ended in {}".format(endTrial.date()))
            os.remove("armwinner.exe.manifest")


    def initUI(self): 
        # PATH = "design_main.ui"
        # PATH = os.path.abspath("design_main_window.ui")              
        # loadUi(PATH, self)
        self.setupUi(self)
        # self.statusBar().showMessage('Ready')
        # self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ArmWinner beta (Dev by Evgeniy Yarmilko)')    
        self.show()
    
    def setCore(self):
        self.initUI()
        self.deleteFromFirstTourTV.clicked.connect(self.deleteFromFirstTourOnClick)
        # main bar actions connections
        self.saveAsAction.triggered.connect(self.saveTableAction)
        self.saveMainTM.triggered.connect(self.saveMaintTMAction)
        self.saveReport.triggered.connect(self.saveReportAction)

        self.openAction.triggered.connect(self.openTableAction)
        # btn connections
        self.addNewPlayerButton.clicked.connect(self.openAddWindowOnClick)
        self.firstTourBtn.clicked.connect(self.startChampOnClick)
        self.addPlayerFromMainTVBtn.clicked.connect(self.addPlayerToFirstTourOnClick)
        self.deleteFromFirstTourTV.clicked.connect(self.deleteFromFirstTourOnClick)
        self.deleteFromMainTM.clicked.connect(self.deleteFromMainTMOnClick)
        ## set table models
        ## main table models
        self.mainTM = MainPlayersTM(tableView=self.tableView)
        self.tableView.setModel(self.mainTM.tableModel)
        self.mainTM.customizeTableViewUI(self.tableView)

        # initilize first tour table model
        
        self.firstTourTM = EliminationTMDLL(self.tour1ATV, type=ModelTypes.FIRST_TOUR)
        self.tour1ATV.setModel(self.firstTourTM.tableModel)
        self.firstTourTM.customizeTableViewUI(self.tour1ATV)
        
    def openTableAction(self):
        path = QFileDialog.getOpenFileName(self, 'Open file', '', 'txt files (*.json)')
        if path and len(path[0]) > 0:
            filePath = str(path[0])

            jsonReader = json_report.ReadJSON(filePath=filePath)
            json = jsonReader.read()

            # clear the model
            self.mainTM.updateView()

            # populate model with data
            for row in json["player_long"]:
                self.mainTM.addDataDict(row)
        else:
            self.showAlertMsg("Предуприждение", "Выбирите путь к файлу")

    def saveMaintTMAction(self):
        path = QFileDialog.getSaveFileName(self, 'Save file', '', 'txt files (*.xlsx)')
        print(path[0])
        filePath = str(path[0])
        if path and len(path[0]) > 0:
            # get data from the main model
            modelData = self.mainTM.getModelData()
            # create json and excel files
            print(filePath + ".json")
            print(filePath + ".xlsx")
            
            writeJSON = json_report.WriteJSON(filePath=filePath + ".json")
            savedFile = writeJSON.saveMainTM(modelData=modelData)
            print(savedFile)
            # create xls
            # excelWriter = json_report.WriteExcel(filePath)
            # excelWriter.createSheet(data=savedFile, createChamp=False)
            # print(filePath)

    def saveReportAction(self):
        path = QFileDialog.getSaveFileName(self, 'Save file', '', 'txt files (*.html)')
        print(path[0])
        filePath = str(path[0])
        if path and len(path[0]) > 0:
            # get data from the main model
            modelData = self.mainTM.getModelData()
            # TODO: get the data from all champ models 
            champData = []
            if self.champDialog is not None:
                modelData = self.mainTM.getModelData()
                champDLL = self.champDialog.iterator.champTMDLL

                writeJSON = json_report.WriteJSON(filePath=filePath + ".json")
                json = writeJSON.saveMainTM(modelData=modelData)
            
                sortedJSON = sorted(json["player_long"], key=lambda x: int(x["место"]), reverse=False)
                # clear the model and populate empty model 
                self.mainTM.updateView()

                for row in sortedJSON:
                    self.mainTM.addDataDict(row)

                savedFile = writeJSON.saveChampTM(modelDataDLL=champDLL)


                # create xls
                htmlWriter = json_to_html.JsonToHtml()
                htmlWriter.createHtml(path=filePath, json=savedFile)
                # excelWriter = helper.WriteExcel(filePath)
                # excelWriter.createSheet(data=savedFile, createChamp=True)

    def saveTableAction(self):
        def populateTXT(fileName, data):
            a = ""
            text_file = open(fileName, "w")
            for number in range(len(data)):
                for index in range(len(data[number])):
                    value = data[number][index]
                    a += str(value) + "\t"
                a += "\n"
            text_file.write(a)
            text_file.close()
    
        path = QFileDialog.getSaveFileName(self, 'Save file', '', 'txt files (*.txt)')
        print(path[0])
        filePath = str(path[0])
        if path and len(path[0]) > 0:
            print(filePath)
            populateTXT(filePath, self.mainTM.getModelData())

    def openAddWindowOnClick(self):
        self.addPlayerWindow = PlayerAdd(parent=self,flags=Qt.WindowTitleHint and Qt.WindowCloseButtonHint)
        self.addPlayerWindow.show()

    def addPlayerToFirstTourOnClick(self):
        # try:
        # check the combo box to check auto/hand input
        firstTourIndex = self.firstTourAddingCB.currentIndex()
        if firstTourIndex == 0: # auto input checkbox
            if self.mainTM.getRowCount() == 0: # if empty
                self.showAlertMsg("Предуприждение", "Введите данные в таблицу")
            else:
                # sort main table view and add changes to the main table model
                self.mainTM.sort()
                for row in self.mainTM.getModelData():
                    self.firstTourTM.addData(row[0])
        else:                   # hand input checkbox
            index = self.tableView.selectedIndexes()

            if index is None or len(index) == 0 or len(index) > 1:
                self.showAlertMsg("Предуприждение", "Выбирите одного игрока с таблицы")
            else:
                row = index[0].row()
                data = self.mainTM.tableModel.data(self.mainTM.tableModel.index(row, 0))
                self.mainTM.colorItem(row, 0)
                self.firstTourTM.addData(data)
        # except Exception as e:
        #     self.showAlertMsg("Ошибка", "Введите жереб. номер всех игроков")

    def startChampOnClick(self):
        # rowNumber = self.mainTM.getRowCount()
        rowNumber = self.firstTourTM.getRowCount()


        if rowNumber >= 2:
            temp = []
            for row in range(rowNumber):
                index = self.firstTourTM.tableModel.index(row, 1)
                # We suppose data are strings
                name = self.firstTourTM.tableModel.data(index)
                temp.append(name)

            # temp = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

            if len(temp) % 2 == 1:
                temp.append(None)
            
            try :
                self.champDialog = PlayingPair(parent=self, flags=Qt.WindowTitleHint and Qt.WindowCloseButtonHint)
                self.champDialog.exec_()
            except Exception as e:
                self.showAlertMsg("Предуприждение", e)

            # set able the 1st tour table
            # self.groupBoxTour1.setEnabled(True)
        else:
            self.showAlertMsg("Предуприждение", "Добавьте больше участников в первый тур")

    def deleteFromFirstTourOnClick(self):
        if self.mainTM.getRowCount() >= 2:
            # get selected index from tableview
            index = self.tour1ATV.selectedIndexes()
            if index is None or len(index) == 0 or len(index) > 1:
                self.showAlertMsg("Предуприждение", "Выбирите одного игрока с таблицы 1го тура")
                pass
            else:
                self.firstTourTM.removeData(index)
        else:
            self.showAlertMsg("Предуприждение", "Добавьте больше игроков в главную таблицу")

    def deleteFromMainTMOnClick(self):
        # get selected index from tableview
        index = self.tableView.selectedIndexes()
        if index is None or len(index) == 0 or len(index) > 1:
            self.showAlertMsg("Предуприждение", "Выбирите одного игрока с главной таблицы")
        else:
            self.mainTM.removeData(index)

    # helper function that is used in PlayerAdd Dialog
    def addInfoToMainTM(self, player):
        self.mainTM.addDataDict(player)

    # helper function to show popup messages
    @staticmethod
    def showAlertMsg(title, msg):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(str(title))
        msgBox.setText(str(msg))
        msgBox.exec_()

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = Main()
        sys.exit(app.exec_())
    except:
        ex.showAlertMsg("Закрытие окна", "Окно закрыто")