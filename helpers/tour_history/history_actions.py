class WrapperAction:
    def __init__(self, action1=None, action2=None, action3=False):
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3 # score update
    
    def __str__(self):
        return "1st Action player {}     2d Action player {}".format(self.action1, self.action2)

class SaveAction:
    def __init__(self, player, model, row):
        self.player = player
        self.model = model
        self.row = row
    
    def __str__(self):
        return self.player

class SaveScoreAction:
    def __init__(self, player, rowInMainTM):
        self.player = player
        self.position = rowInMainTM