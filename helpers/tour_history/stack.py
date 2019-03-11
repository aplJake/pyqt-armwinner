from .history_actions import WrapperAction, SaveAction


class Stack:
    def __init__(self, tourID=None):
        self.items = []
        self.tourID = tourID
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        print("Check whether empty")
        print((self.items == []))
        return (self.items == [])
    
    def __str__(self):
        str = " "
        for item in self.items:
            if item.action1 is not None: 
                player1 = item.action1.player
            else:
                player1 = "1-"

            if item.action2 is not None: 
                player2 = item.action2.player
            else:
                player2 = "2-"

            str += player1 + " " + player2 + "\n"
        return str
    
    @staticmethod
    def test():
        s = Stack()

        save1 = SaveAction("player1", 1, 1)
        save2 = SaveAction("player2", 2, 1)
        save3 = SaveAction("player3", 1, 2)
        save4 = SaveAction("player4", 2, 2)
        

        s.push(WrapperAction(save1, save2))
        s.push(WrapperAction(save3, save4))

        print("PEEK", s.peek())
        s.output()
        s.pop()
        # s.output()
        print(s)