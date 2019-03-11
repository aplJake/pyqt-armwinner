from .stack import Stack
from PyQt5.QtGui import QStandardItem
class StackController(Stack):

    currentHighscore = None
    mainTableModel = None

    def __init__(self, capacity=None, mainTableModel=None, tourID=None):
        self.currentHighscore = capacity
        self.mainTableModel = mainTableModel
        return super().__init__(tourID=tourID)
    
    def pop(self):
        if len(self.items) > 0:
            # update score index
            # find peek item and search it in main table
            # delete from main table
            self.updateOnDelete()
            # self.currentHighscore += 1
            return super().pop()
    
    def push(self, item):
        if self.currentHighscore > 0: 
            self.updateOnAdd(item)
            # self.currentHighscore -= 1
            return super().push(item)

    def updateOnAdd(self, item):
        self.mainTableModel.setItem(item.action1.position, 5, QStandardItem(str(self.currentHighscore)))
        self.currentHighscore -= 1

        if item.action2 is not None:
            self.mainTableModel.setItem(item.action2.position, 5, QStandardItem(str(self.currentHighscore))) 
            self.currentHighscore -= 1  


    def updateOnDelete(self):
        
        item = self.peek()
        self.mainTableModel.setItem(item.action1.position, 5, QStandardItem())
        self.currentHighscore += 1
        if item.action2 is not None:
            self.mainTableModel.setItem(item.action2.position, 5, QStandardItem())
            self.currentHighscore += 1
    
    def __str__(self):
        s = ""
        for saveScoreItem in self.items:
            s += saveScoreItem.action1.player + str(saveScoreItem.action1.position) + "\n"
            if saveScoreItem.action2 is not None:
                s += saveScoreItem.action1.player + str(saveScoreItem.action1.position) + "\n"

        return s