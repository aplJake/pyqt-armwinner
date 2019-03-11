from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

# from table_objects import Player
from .design import Ui_addPlayerQObject

class PlayerAdd(QDialog, Ui_addPlayerQObject):
    def __init__(self, parent=None, flags=None):
        super(PlayerAdd, self).__init__(parent, flags)
        # empty player data to transfer for
        self.playerData = []
        self.setInitUI()
        '''
        BUTTON CONNECTIONS
        '''
        self.addPlayerBtn.clicked.connect(self.addPlayerAction)
        self.cancelAddPlayerBtn.clicked.connect(self.cancelAddPlayerAction)

    def setInitUI(self):
        # PATH = "design_user_adding.ui"
        # loadUi(PATH, self)
        self.setupUi(self)


    def addPlayerAction(self):
        playerName = self.nameLineEdit.text()
        playerIdNumber = self.idNumberTextEdit.text()
        playerTeam = self.teamLineEdit.text()
        playerQual = self.qualLineEdit.text()
        playerWeight = self.weightLineEdit.text()

        if playerName and playerTeam and playerQual and playerWeight:
            playerData = {
                'name': playerName,
                'qualification': playerQual,
                'team': playerTeam,
                'weight': playerWeight
            }

            #  name, qualification="qual", team="team", weight=85, id_number=5, score=0
            # player = Player(playerName, playerQual, playerTeam, playerWeight, playerIdNumber)
            self.parent().addInfoToMainTM(playerData)
            self.close()
            # add data to the table
            # return player.__dict__
            return playerData
        else:
            self.showAlertMsg("Предупреждение", "Введите все данные об участнике")
            return None

    def getPlayerData(self):
        return self.playerData

    def cancelAddPlayerAction(self):
        self.close()