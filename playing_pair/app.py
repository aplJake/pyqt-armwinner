from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QColor
from PyQt5.QtCore import Qt

from .design import Ui_Fighting
from .table_model import PlayingPairTM
from .window_controller import ChampTableIterator


# from table_models import EliminationTMDLL, SaveAction, Stack, SaveScoreAction, StackController, WrapperAction
# from buffer_linked_list import QDialogController
# from buffer_linked_list import ModelTypes

class PlayingPair(QDialog, Ui_Fighting):
    def __init__(self, parent=None, flags=None):
        super(PlayingPair, self).__init__(parent, flags)
        self.setInitUI()

        # create the iterator object for iteration between players objects
        #  and creation the new model items
        self.qDialogTM = PlayingPairTM(self.pairTableView)
        self.pairTableView.setModel(self.qDialogTM.tableModel)
        self.iterator = ChampTableIterator(
            qDialogTM=self.qDialogTM, parent=self.parent())

        '''
        BUTTON CONNECTIONS
        '''
        self.wonFirstPlayerBtn.clicked.connect(self.firstPlayerWonOnClick)
        self.wonSecondPlayerBtn.clicked.connect(self.secondPlayerWonOnClick)

        self.backTourBtn.clicked.connect(self.backTourAction)
        # self.nextTourBtn.clicked.connect(self.nextTourAction)

    def setInitUI(self):
        # PATH = "design_playing_pair.ui"
        # loadUi(PATH, self)
        self.setupUi(self)

    def firstPlayerWonOnClick(self):
        # self.iterator.winFirst()

        try:
            self.iterator.winFirst()
        except Exception as e:
            self.showAlertMsg("Warning", f"Error {e}")

    def secondPlayerWonOnClick(self):
        # self.iterator.winSecond()
        try:
            self.iterator.winSecond()
        except Exception as e:
            self.showAlertMsg("Warning", f"Error type 2 {e}")

    def backTourAction(self):
        # self.iterator.returnModelHistory()
        try:
            self.iterator.returnModelHistory()
        except Exception as e:
            self.showAlertMsg("Warning", f"Error type 3 {e}")
