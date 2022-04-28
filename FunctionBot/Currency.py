import json
import os

from prettytable import PrettyTable

class Currency:

    def __init__(self, PATH):
        self.PATH = PATH

    def readFileJson(self):
        try:
            with open(self.PATH + '/data_currency.json','r', encoding="utf-16") as f:
                data = json.load(f)
            table = PrettyTable(["Ngoại tệ", "Mua tiền mặt", "Mua chuyển khoản", "Giá bán"])
            
            text = data[0]['Thời gian cập nhật'].split(".")[0] 
            lst = text.split()
            title = ""
            for i in range(5, len(lst)):
                title += lst[i].title() + " "
            table.title = title.strip()
            for element in range (1, len(data)):
                lst = []
                for value in data[element].values():
                    lst.append(value)
                table.add_row([lst[0], lst[1], lst[2], lst[3]])
            
            return table
        except IOError as ex:
            print("%s" % ex)


if __name__ == "__main__":
    test = Currency()
    print(test.readFileJson())