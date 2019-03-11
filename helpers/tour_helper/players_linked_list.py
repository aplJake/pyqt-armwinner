
class PlayingPair:
    def __init__(self, pair: list):
        self.firstPlayer = pair[0]
        self.secondPlayer = pair[1]
    
    def getPairAsList(self):
        return [self.firstPlayer, self.secondPlayer]
    
class PairNode:
    def __init__(self, data: PlayingPair, prevPair: PlayingPair, nextPair: PlayingPair):
        self.data = data
        self.prevPair = prevPair
        self.nextPair = nextPair

class DoublePlayersPairList:
    head = None
    tail = None

    def append(self, tour: PlayingPair):
        newNode = PairNode(tour, None, None)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prevPair = self.tail
            newNode.nextPair = None
            self.tail.nextPair = newNode
            self.tail = newNode

    def remove(self, nodeValue: PlayingPair):
        currentNode = self.head

        while currentNode is not None:
            if currentNode.data == nodeValue:
                # if it is not the first element
                if currentNode.prevPair is not None:
                    currentNode.prevPair.nextPair = currentNode.nextPair
                    currentNode.nextPair.prevPair = currentNode.prevPair
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = currentNode.nextPair
                    currentNode.nextPair.prevPair = None
    
    # add node at the from of the list
    def push(self, nodeValue: PlayingPair):
        newNode = PairNode(nodeValue, None, None)

        newNode.nextPair = self.head
        newNode.prevPair = None

        if self.head is not None:
            self.head.prevPair = newNode
        
        self.head = newNode


    def show(self):
        print("Show list data")
        currentNode = self.head

        while currentNode is not None:
            print(currentNode.data.getPairAsList())
            currentNode = currentNode.nextPair
            print("*"*50)