import io, json

class TestJSONTempFile:
    def test(self):
        filePath = "D:\Repos Projects\ArmWinnerTestv1\ArmWinnerMain\ArmWinnerMain\myjson.json"
        datain = [
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ]
        champData = [
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4", "item5"],
            ["item1", "item2", "item3", "item4", "item5", "item6"],
            ["item1", "item2", "item3", "item4"],
            ["item1", "item2", "item3"],
            ["item1", "item2"]
        ]

        j = WriteJSON(filePath)
        j.saveMainTM(modelData=datain)
        j.saveChampTM(modelData=champData)

        r = ReadJSON(filePath)
        data = r.read()

        # WriteExcel(filePath).createSheet(data=data)

class WriteJSON:
    def __init__(self, filePath=None, parent=None):
        self.filePath = filePath
        self.parent = parent

        # create file for main table and secondary table
        self.reportMainJSON = {}
        self.reportSecondaryJSON = {}

    # save to json adata about main table
    def saveMainTM(self, modelData):
        self.reportMainJSON["player_long"] = []

        for rowData in modelData:
            self.reportMainJSON["player_long"].append({
                "имя":                  str(rowData[0]),
                "квалификация":         str(rowData[1]),
                "команда":              str(rowData[2]),
                "вес":                  str(rowData[3]),
                "номер":                str(rowData[4]),
                "место":                str(rowData[5])
            })
        if self.filePath is None:
            return self.reportMainJSON
        else:
            self.saveJSONInFile()
            return self.reportMainJSON
    
    #  save json data about champ tours
    def saveChampTM(self, modelDataDLL):        
        self.reportMainJSON["player_short"] = []

        # iterate over models in dll
        currentNode = modelDataDLL.head
        while currentNode.nextTour is not None:
            modelData = currentNode.data.getWinnerModelData()

            tmpDict = {}
            tmpDict["players"] = []
            for item in modelData:
                print(f"This item: {item}")
                tmpDict["players"].append({
                    # "номер":             "1",
                    "имя":          str(item[0]),
                    "статус":        str(item[1])
                })
            self.reportMainJSON["player_short"].append(tmpDict)
            # update mode to next
            currentNode = currentNode.nextTour
        # print("AIM REPORT")
        # print(self.reportMainJSON)
        self.saveJSONInFile()
        return self.reportMainJSON
    
    def saveJSONInFile(self):
        # save into html
        
        # save to file
        with io.open(self.filePath, "w", encoding="utf8") as file:
            json.dump(self.reportMainJSON, file, ensure_ascii=False)



class ReadJSON:
    def __init__(self, filePath):
        self.filePAth = filePath
    
    def read(self):
        with io.open(self.filePAth, encoding="utf8") as file:
            data = json.load(file)
        # pprint.pprint(data)
        return data # returns json