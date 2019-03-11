
class TourNode:
    def __init__(self, data, prevTour, nextTour):
        self.data = data
        self.prevTour = prevTour
        self.nextTour = nextTour


class DoubleTourList:
    head = None
    tail = None

    def append(self, tour):
        newNode = TourNode(tour, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prevTour = self.tail
            newNode.nextTour = None
            self.tail.nextTour = newNode
            self.tail = newNode

    def remove(self, nodeValue):
        currentNode = self.head

        while currentNode is not None:
            if currentNode.data == nodeValue:
                # if it is not the first element
                if currentNode.prevTour is not None:
                    currentNode.prevTour.nextTour = currentNode.nextTour
                    currentNode.nextTour.prevTour = currentNode.prevTour
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = currentNode.nextTour
                    currentNode.nextTour.prevTour = None

    def getSemiFinalModel(self):
        return self.getFinalModel().prevTour
        
    def getFinalModel(self):
        return self.getGrandFinalModel().prevTour

    def getGrandFinalModel(self):
        return self.tail

    def show(self):
        currentNode = self.head
        while currentNode is not None:
            print("Model type", currentNode.data.modelType)
            print(currentNode.data.stackHistory)
            currentNode = currentNode.nextTour
            print("*"*50)
