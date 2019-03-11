from PyQt5.QtGui import QStandardItem, QColor
from PyQt5.QtCore import Qt

from helpers.enums.champ_model_types import ModelTypes
from helpers.tour_helper.tour_linked_list import DoubleTourList
from main.champ_table_model import EliminationTMDLL
from helpers.tour_history.stack_controller import StackController
from helpers.tour_history.history_actions import WrapperAction, SaveAction, SaveScoreAction

# from playing_pair
class ChampTableIterator:

    isFinal = False
    hasGrandfinal = False
    scoreHistoryStack = None

    def __init__(self, qDialogTM, parent=None):
        # define champ models object
        self.champTMDLL = DoubleTourList()
        self.champTMDLL.append(parent.firstTourTM)
        self.champTMDLL.append( EliminationTMDLL(parent.tour2ATM, type=ModelTypes.SECOND_TOUR_A) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour2BTM, type=ModelTypes.SECOND_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour3ATM, type=ModelTypes.THIRD_TOUR_A) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour3BTM, type=ModelTypes.THIRD_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour4ATM, type=ModelTypes.FOURTH_TOUR_A) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour4BTM, type=ModelTypes.FOURTH_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour5ATM, type=ModelTypes.FIFTH_TOUR_A) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour5BTM, type=ModelTypes.FIFTH_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour6BTM, type=ModelTypes.SIXTH_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour7BTM, type=ModelTypes.SEVENTH_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour8BTM, type=ModelTypes.EIGHTH_TOUR_B) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour6ATM, type=ModelTypes.SEMI_FINAL_TOUR) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour7ATM, type=ModelTypes.FINAL_TOUR) )
        self.champTMDLL.append( EliminationTMDLL(parent.tour8ATM, type=ModelTypes.GRAND_FINAL_TOUR) )

        # create history
        self.scoreHistoryStack = StackController(capacity=parent.firstTourTM.getRowCount(), 
                                                mainTableModel=parent.mainTM.tableModel)
        # history = History()

        # current node
        # initially we set current node to the head node
        self.currentTourNode = self.champTMDLL.head

        self.placeID = parent.firstTourTM.getRowCount()
        self.parent = parent
        self.qDialogTM = qDialogTM

        # show initially plaing pair in QDialog
        self.currentTourNode.data.formPlayingPairs()
        pair = self.currentTourNode.data.currentPairNode.data.getPairAsList()
        self.qDialogTM.updateTableData(pair)



    def updateCurrentTourNode(self):
        self.currentTourNode = self.currentTourNode.nextTour

        if self.currentTourNode.data.currentPairNode is None:
            self.updateCurrentTourNode()
        else:
            self.currentTourNode.data.formPlayingPairs()
            # update the view in QDialog
            pair = self.currentTourNode.data.currentPairNode.data.getPairAsList()
            self.qDialogTM.updateTableData(pair)

    def winFirst(self):
        # playingPair = self.currentTourNode.data.getModelData()

        winner = self.qDialogTM.getFirstPlayer()
        loser = self.qDialogTM.getSecondPlayer()

        self.__handlePair(winner, loser)

    def winSecond(self):
        winner = self.qDialogTM.getSecondPlayer()
        loser = self.qDialogTM.getFirstPlayer()

        self.__handlePair(winner, loser)

    def colorWinner(self, item: QStandardItem, color=QColor(127, 255, 0)):
        # font = QFont()
        # font.setUnderline(True)
        # item.setFont(font)
        item.setBackground(QColor(223, 223, 223))

    def findItem(self, itemToSearch, modelToSearch):
        pass

    # Helping method for updating and adding winner loser data
    # is used as a seperate function as it has the same actions as winSecond()
    def __handlePair(self, winner: str, loser: str):
        def updateDialog():
            # try update the pair
            isUpdated = self.currentTourNode.data.updateCurrentPair()
            if not isUpdated:
                # if we cannot to update the pair then it it the end of the model and we update the model
                self.updateCurrentTourNode()
                self.currentTourNode.data.formPlayingPairs()

            # update the view in QDialog
            pair = self.currentTourNode.data.currentPairNode.data.getPairAsList()
            self.qDialogTM.updateTableData(pair)

        # color the winner
        currentModel = self.currentTourNode.data
        winnerRow = self.findPlayer(currentModel.tableModel, winner, column=1)
        loserRow = self.findPlayer(currentModel.tableModel, loser, column=1)
        # currentModel.item(winnerRow, 0).setBackground(QColor(148, 255, 45))
        currentModel.tableModel.item(
            winnerRow, 1).setBackground(QColor(190, 255, 127))
        print("MAIN LOG OF COLORING: winnerName: {} winnerRow: {} modelType: {}".format(
            winner, winnerRow, self.currentTourNode.data.modelType))
        # match the winner in winner column
        currentModel.isWinner(winnerRow, "Чемп.")
        if loserRow is not None:
            currentModel.isWinner(loserRow, "Проиг.")


        modeType = self.currentTourNode.data.modelType

        if modeType is (ModelTypes.FIRST_TOUR):
            modelA = self.currentTourNode.nextTour
            modelB = modelA.nextTour
            if self.currentTourNode.data.currentPairNode.data.secondPlayer == None:
                player = self.currentTourNode.data.currentPairNode.data.firstPlayer
                modelA.data.push(player)
            else:
                # add history
                action1 = SaveAction(player=winner, model=modelA, row=modelA.data.getRowCount())
                action2 = SaveAction(player=loser, model=modelB, row=modelB.data.getRowCount())
                self.currentTourNode.data.addHistoryAction(action1, action2)

                modelA.data.addData(winner)
                modelB.data.addData(loser)
    
            updateDialog()
        elif modeType in (ModelTypes.SECOND_TOUR_A, ModelTypes.THIRD_TOUR_A, ModelTypes.FOURTH_TOUR_A, ModelTypes.FIFTH_TOUR_A):
            if self.currentTourNode.data.getRowCount() > 2:
                modelA = self.currentTourNode.nextTour.nextTour
                modelB = modelA.nextTour
            else:
                modelA = self.champTMDLL.getFinalModel()
                modelB = self.champTMDLL.getSemiFinalModel()

            if self.currentTourNode.data.currentPairNode.data.secondPlayer == None:
                player = self.currentTourNode.data.currentPairNode.data.firstPlayer
                # add history
                action1 = SaveAction(player=player, model=modelA, row=0)
                self.currentTourNode.data.addHistoryAction(action1)

                modelA.data.push(player)
            else:
                # add history
                action1 = SaveAction(player=winner, model=modelA, row=modelA.data.getRowCount())
                action2 = SaveAction(player=loser, model=modelB, row=modelB.data.getRowCount())
                self.currentTourNode.data.addHistoryAction(action1, action2)

                modelA.data.addData(winner)
                modelB.data.addData(loser)
            updateDialog()
        elif modeType in (ModelTypes.SECOND_TOUR_B, ModelTypes.THIRD_TOUR_B, ModelTypes.FOURTH_TOUR_B):
            if self.currentTourNode.data.getRowCount() > 2:
                modelB = self.currentTourNode.nextTour.nextTour
            else:
                modelB = self.champTMDLL.getSemiFinalModel()

            if self.currentTourNode.data.currentPairNode.data.secondPlayer == None:
                player = self.currentTourNode.data.currentPairNode.data.firstPlayer
                # add history
                action1 = SaveAction(player=player, model=modelB, row=0)
                self.currentTourNode.data.addHistoryAction(action1)

                modelB.data.push(player)
            else:
                # add history
                action2 = SaveAction(player=winner, model=modelB, row=modelB.data.getRowCount())
                self.currentTourNode.data.addHistoryAction(action2, action3=True)

                modelB.data.addData(winner)
                

                # update score
                loserRow = self.findPlayer(self.parent.mainTM.tableModel, loser)
                self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow)))

                # self.parent.mainTM.tableModel.setItem(loserRow, 5, QStandardItem(str(self.placeID)))
                # self.placeID -= 1
            updateDialog()
        elif modeType in (ModelTypes.FIFTH_TOUR_B, ModelTypes.SIXTH_TOUR_B, ModelTypes.SEVENTH_TOUR_B, ModelTypes.EIGHTH_TOUR_B):
            if self.currentTourNode.data.getRowCount() > 2:
                modelB = self.currentTourNode.nextTour
            else:
                modelB = self.champTMDLL.getSemiFinalModel()

            if self.currentTourNode.data.currentPairNode.data.secondPlayer == None:
                player = self.currentTourNode.data.currentPairNode.data.firstPlayer

                # add history
                action1 = SaveAction(player=player, model=modelB, row=0)
                self.currentTourNode.data.addHistoryAction(action1)

                modelB.data.push(player)
            else:
                # add history
                action2 = SaveAction(player=winner, model=modelB, row=modelB.data.getRowCount())
                self.currentTourNode.data.addHistoryAction(action2, action3=True)

                modelB.data.addData(winner)
                # update score
                loserRow = self.findPlayer(self.parent.mainTM.tableModel, loser)

                self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow)))

                # self.parent.mainTM.tableModel.setItem(loserRow, 5, QStandardItem(str(self.placeID)))
                # self.placeID -= 1
            updateDialog()
        elif modeType is (ModelTypes.SEMI_FINAL_TOUR):
            modelA = self.currentTourNode.nextTour

            # add history
            action1 = SaveAction(player=winner, model=modelA, row=modelA.data.getRowCount())
            self.currentTourNode.data.addHistoryAction(action1, action3=True)

            modelA.data.addData(winner)
            # update score
            loserRow = self.findPlayer(self.parent.mainTM.tableModel, loser)

            self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow)))

            # self.parent.mainTM.tableModel.setItem(loserRow, 5, QStandardItem(str(self.placeID)))
            # self.placeID -= 1
            updateDialog()
        elif modeType is (ModelTypes.FINAL_TOUR):
            if winner == self.currentTourNode.data.currentPairNode.data.secondPlayer:
                modelA = self.currentTourNode.nextTour
                # add history
                action1 = SaveAction(player=winner, model=modelA, row=modelA.data.getRowCount())
                action2 = SaveAction(player=loser, model=modelA, row=modelA.data.getRowCount())
                self.currentTourNode.data.addHistoryAction(action1, action2)

                modelA.data.addData(winner)
                modelA.data.addData(loser)
                
                self.champTMDLL.show()
                print("Score history stack\n\n")
                print(self.scoreHistoryStack)
                updateDialog()
            else:
                # update score
                loserRow = self.findPlayer(self.parent.mainTM.tableModel, loser)
                # self.parent.mainTM.tableModel.setItem(loserRow, 5, QStandardItem(str(2)))
                # self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow)))

                # update score
                winnerRow = self.findPlayer(self.parent.mainTM.tableModel, winner)
                # self.parent.mainTM.tableModel.setItem(winnerRow, 5, QStandardItem(str(1)))
                # self.scoreHistoryStack.push(SaveScoreAction(winner, winnerRow))
                self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow), SaveScoreAction(winner, winnerRow)))


        elif modeType is ModelTypes.GRAND_FINAL_TOUR:
            # update score
            loserRow = self.findPlayer(self.parent.mainTM.tableModel, loser)
            # self.parent.mainTM.tableModel.setItem(loserRow, 5, QStandardItem(str(2)))

            # update score
            winnerRow = self.findPlayer(self.parent.mainTM.tableModel, winner)
            # self.parent.mainTM.tableModel.setItem(winnerRow, 5, QStandardItem(str(1)))
            self.scoreHistoryStack.push(WrapperAction(SaveScoreAction(loser, loserRow), SaveScoreAction(winner, winnerRow)))
        else: 
            raise ValueError

    def findPlayer(self, model, playerName, column=0):
        print("\n\n MATCH LOSER IN THE MODEL")
        start = model.index(0, column)
        matches = model.match(start, Qt.DisplayRole,
                              playerName, 1, Qt.MatchContains)

        if matches:
            index = matches[0]
            row = index.row()
            # index.row(), index.column()
            return row

    def log(self, msg):
        print("*"*50)
        print(f"{msg}")
        print("*"*50)

    def returnModelHistory(self):

        def updateDialog():
            # update data in QDialog
            pair = self.currentTourNode.data.currentPairNode.data.getPairAsList()
            print(f"QDIALOG pair {pair}")
            self.qDialogTM.updateTableData(pair)
            # update color of the current pair in the model
            # setDefaultPairColor(model=self.currentTourNode.data.tableModel)


        print("Works return history!")
        print("Current model type is {}".format(self.currentTourNode.data.modelType))
        print("Stack history is")
        print(self.currentTourNode.data.stackHistory)
        if self.currentTourNode.data.stackHistory.isEmpty():
            print("Stack is empty!")

            if self.currentTourNode.prevTour is not None:
                self.currentTourNode = self.currentTourNode.prevTour
                self.returnModelHistory()
            else: 
                print("Stack is not empty!")

        else:
            print("Stack is full!")

            # unpack action1 and action2
            wrraperAction = self.currentTourNode.data.stackHistory.peek()
            # get data for model row for action1 action2
            action1 = wrraperAction.action1
            action2 = wrraperAction.action2
            action3 = wrraperAction.action3

            # delete data1 
            if action1 is not None:

                print("action1")
                action1.model.data.removeRow(row=action1.row)


                playerRow = self.findPlayer(self.currentTourNode.data.tableModel, action1.player, column=1)
                self.currentTourNode.data.tableModel.item(playerRow, 1).setBackground(QColor(255, 255, 255))
            else: 
                print("action1 not")

                pass
            # delete data2
            if action2 is not None:
                print("action2")
                action2.model.data.removeRow(row=action2.row)
                
            else:
                print("action2 not")
                

                pass

            #update score
            if action3 is True: 
                print("****************ACtion 3 is true ")
                print(self.scoreHistoryStack)

            else:
                print("****************ACtion 3 NOT true ")
                print(self.scoreHistoryStack)


                self.scoreHistoryStack.pop()
            self.currentTourNode.data.realeseHistoryAction()

            if self.currentTourNode.data.currentPairNode.prevPair is not None:
                self.currentTourNode.data.currentPairNode = self.currentTourNode.data.currentPairNode.prevPair
            
            if self.currentTourNode.data.currentPairNode is not None:
                print("case 23 5")
                updateDialog()
            else:
                print("case 23 4")

                # change tour 
                # if tour1 set on it
                pass