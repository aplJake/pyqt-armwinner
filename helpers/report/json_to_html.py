import json, pprint

class JsonToHtml:
    # filePAth: path of json file
    def __init__(self):
        pass
    
    def generateMainTable(self):
        pass
    
    def generateFullReport(self):
        pass
    
    def read(sel, filePath):
        file = open(filePath, "r", encoding="utf8")
        data = json.load(file)
        file.close()

        # pprint.pprint(data)
        return data # returns json

    def createHtml(self, path, json, both=True):
        # json = self.read(self.filePath)
        try:
            f = open(path, "w", encoding="utf8")
            f.write('<!doctype html>')
            f.write('<html lang="en">')
            f.write('<head>')
            f.write('<meta http-equiv="X-UA-Compatible" content="ie=edge" charset="UTF-8">')
            f.write('</head>')
            f.write('<body>')
            f.write('<h4>Отчет</h4>')

            # creating table
            # f.write('<h5>Главная таблица</h5>')

            f.write('<table border = "1" cellpadding=1 cellspacing=0 style="font-family: Times, Serif; font-size: 12px">')
            f.write('<tr>')
            # f.write('<th>№</th>')
            f.write('<th>Участник</th>')
            f.write('<th>Квалификация</th>')
            f.write('<th>Команда</th>')
            f.write('<th>Вес</th>')
            f.write('<th>Ж/н</th>')
            f.write('<th>Место</th>')
            f.write('</tr>')

            data = json["player_long"]
            for obj in json["player_long"]:
                f.write("<tr>")
                for key, val in obj.items():
                    print(key, val)
                    f.write(f"<td> {val} </td>")
                f.write("</tr>")
            f.write('</table>')
            # end       creating table

            if both is True:
                tourNames = [
                    "Тур1", 
                    "Тур2а", "Тур2б",
                    "Тур3а", "Тур3б",
                    "Тур4а", "Тур4б",
                    "Тур5а", "Тур5б", "Тур6б", "Тур7б",
                    "Тур8б",
                    "Полуфинал", 
                    "Финал",
                    "Суперфинал"
                ]
                aTourNames = [
                    "Тур2а",
                    "Тур3а",
                    "Тур4а",
                    "Тур5а",
                    "Полуфинал",
                    "Финал",
                    "Суперфинал"
                ]
                bTourNames = [
                    "Тур2б",
                    "Тур3б",
                    "Тур4б",
                    "Тур5б",
                    "Тур6б",
                    "Тур7б",
                    "Тур8б"
                ]
                firstTour = []
                evenTours = []
                oddTours = []
                # creating table
                f.write('<h5>Чемпионат</h5>')


                # sort tours
                tourIndex = 0
                for tour in json["player_short"]:
                    if tourIndex == 0:
                        for players in tour["players"]:
                            firstTour.append(players)
                    elif tourIndex % 2 == 1: # even
                        temp = []
                        for players in tour["players"]:
                            temp.append(players)
                        evenTours.append(temp)
                    else:                    # odd
                        temp = []
                        for players in tour["players"]:
                            temp.append(players)
                        oddTours.append(temp)
                    tourIndex += 1
                
                # populate tours
                ## first tour
                f.write('<div style="float: left">')
                f.write('<table border = "1" cellpadding="4" cellspacing=0 style="margin: 0 1px 1px 0; font-family: Times, Serif; font-size: 8px">')
                f.write('<col>')
                f.write('<colgroup span="2"></colgroup>')
                f.write(f'<tr><th colspan="2" scope="colgroup">Тур1</th></tr>')
                f.write('<tr>')
                f.write('<th scope="col" style="min-width: 90px" >Имя</th>')
                f.write('<th scope="col" >Статус</th>')
                for players in firstTour:
                    f.write("<tr>")
                    for key, value in players.items():
                        f.write(f"<td > {value} </td>")
                    f.write("<tr>")
                f.write('</table>')
                f.write('</div>')


                ## champ tours
                f.write('<div style="float: center">')
                ### even tours
                f.write('<div style="display: flex">')
                print("2x tour")
                print(evenTours)
                hindex = 0
                for tour in evenTours:
                    print(f"\n\n\n\nPlayers {len(tour)}")

                    
                    f.write('<table border = "1" cellpadding="2" cellspacing=0 style="margin: 0 1px 1px 0 ; font-family: Times, Serif; font-size: 8px">')
                    f.write('<col>')
                    f.write('<colgroup span="2"></colgroup>')
                    f.write(f'<tr><th colspan="2" scope="colgroup">{aTourNames[hindex]}</th></tr>')
                    f.write('<tr>')
                    f.write('<th scope="col" style="min-width: 90px" >Имя</th>')
                    f.write('<th scope="col" >Статус</th>')
                    f.write('</tr>')
                    if len(tour) == 0:
                        for i in range(2):
                            f.write("<tr>")
                            f.write(f"<td> {'-'} </td>")
                            f.write(f"<td> {'-'} </td>")
                            f.write("<tr>")
                    else:
                        for players in tour:
                            print(f"\n\n\n\nPlayers {len(tour)}")

                            f.write("<tr>")
                            for key, value in players.items():
                                f.write(f"<td > {value} </td>")
                            f.write("<tr>")
                    f.write('</table>')
                    hindex += 1
                f.write('</div>')

                ### odd tours
                f.write('<div style="display: flex">')
                print("2x tour")
                print(evenTours)
                hindex = 0
                for tour in oddTours:

                    f.write('<table border = "1" cellpadding="2" cellspacing=0 style="margin: 0 1px 1px 0 ; font-family: Times, Serif; font-size: 8px">')
                    f.write('<col>')
                    f.write('<colgroup span="2"></colgroup>')
                    f.write(f'<tr><th colspan="2" scope="colgroup">{bTourNames[hindex]}</th></tr>')
                    f.write('<tr>')
                    f.write('<th scope="col" style="min-width: 90px" >Имя</th>')
                    f.write('<th scope="col" >Статус</th>')
                    f.write('</tr>')
                    if len(tour) == 0:
                        for i in range(2):
                            f.write("<tr>")
                            f.write(f"<td> {'-'} </td>")
                            f.write(f"<td> {''} </td>")
                            f.write("<tr>")
                    else:
                        for players in tour:
                            print(f"\n\n\n\nPlayers {players}")
                            f.write("<tr>")
                            for key, value in players.items():
                                f.write(f"<td> {value} </td>")
                            f.write("<tr>")
                    f.write('</table>')
                    hindex += 1
                f.write('</div>')
                
                f.write('</div>')
 
            f.write('</body>')
            f.write('</html>')
            f.close()


        except(IOError, FileNotFoundError) as identifier:
            print(identifier)

    @staticmethod
    def test():
        PATH = "D:\\Repos Projects\\ArmWinnerTestv1\\ArmWinnerMain\\ArmWinnerMain\\полныйОтчет.xlsx.json"
        OUT_PATH = "D:/Test.html"
        testObj = JsonToHtml()
        testObj.read(PATH)
        testObj.createHtml(OUT_PATH)

if __name__ == "__main__":
    JsonToHtml().test()