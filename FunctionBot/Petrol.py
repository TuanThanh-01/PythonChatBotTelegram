import datetime
from prettytable import PrettyTable
import os

class Petrol:

    def __init__(self):
        os.chdir("../Python Project/Bot_Telegram/Data")
        self.PATH = os.getcwd()
        self.timeNow = str(datetime.date.today().strftime("%d/%m/%Y"))
    
    def getTablePetrolPrice(self):
        try:
            with open(self.PATH + '/data_petrol_price.csv','r', encoding="utf-16") as f:
                result = f.readlines()
                result.pop(0)
            table = PrettyTable(["Sản phẩm", "Vùng 1", "Vùng 2"])
            table.title = "Thông tin giá xăng dầu ngày " + self.timeNow
            for element in result:
                if element != '\n':
                    row = element.replace('\n', "").split(",")
                    if len(row) > 3:
                        row[0] += row[1]
                        row[0] = row[0][1:-1]
                        table.add_row([row[0], row[2], row[3]])
                    else:
                        table.add_row([row[0], row[1], row[2]])
            
            return table
        except IOError as ex:
            print("%s" % ex)

if __name__ == "__main__":
      data = Petrol()
      print(data.getTablePetrolPrice())