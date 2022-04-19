import json
import os

class GoldPrice:

    def __init__(self):
        os.chdir("../PythonProjectPTIT/Data")
        self.PATH = os.getcwd()

    def readFileJson(self):
        try:
            with open(self.PATH + '/data_gold_price.json','r', encoding="utf-16") as f:
                data = json.load(f)
            print(type(data))
            print(data)
        except IOError as ex:
            print("%s" % ex)


if __name__ == "__main__":
    test = GoldPrice()
    test.readFileJson()