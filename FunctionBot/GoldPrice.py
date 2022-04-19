from CrawlData import GoldPriceData
import os

class GoldPrice:

    def __init__(self):
        os.chdir("../Python Project/Bot_Telegram/Data")
        self.PATH = os.getcwd()

    def readFileJson(self):
        try:
            with open(self.PATH + '/data_petrol_price.csv','r', encoding="utf-16") as f:
                pass
        except IOError as ex:
            print("%s" % ex)
    