import json
import os

from prettytable import PrettyTable

class Currency:

    def __init__(self):
        os.chdir("../PythonProjectPTIT/Data")
        self.PATH = os.getcwd()

    def readFileJson(self):
        try:
            with open(self.PATH + '/data_currency.json','r', encoding="utf-16") as f:
                data = json.load(f)
            table = PrettyTable(["Ngoại tệ", "Mua tiền mặt", "Mua chuyển khoản", "Giá bán"])
            
            table.title = data[0]['Thời gian cập nhật'].split(".")[0] 
            # sửa lại sau nhé idol Thành ưi

            for element in range (1, len(data)):
                lst = []
                for value in data[element].values():
                    lst.append(value)
                table.add_row([lst[0], lst[1], lst[2], lst[3]])
            
            print(table)
        except IOError as ex:
            print("%s" % ex)


if __name__ == "__main__":
    test = Currency()
    test.readFileJson()