import json
import os

from prettytable import PrettyTable

class GoldPrice:

    def __init__(self, PATH):
        self.PATH = PATH

    def readFileJson(self):
        try:
            with open(self.PATH + '/data_gold_price.json','r', encoding="utf-16") as f:
                data = json.load(f)
            table = PrettyTable(["Loại vàng", "Giá mua", "Giá bán"])
            
            for key, value in data[0].items():
                table.title = key+ ": "+ value
        
            for element in range (1, len(data)):
                lst = []
                for value in data[element].values():
                    lst.append(value)
                table.add_row([lst[0], lst[1], lst[2]]) 
            
            return table
        except IOError as ex:
            print("%s" % ex)



if __name__ == "__main__":
    test = GoldPrice()
    test.readFileJson()