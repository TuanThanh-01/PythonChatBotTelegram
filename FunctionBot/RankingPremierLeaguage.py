import csv
import datetime
import os
from prettytable import PrettyTable
from selenium import webdriver
from selenium.webdriver.common.by import By

class RankingPremierLeaguage:

    def __init__(self, PATH):
        self.PATH = PATH
        self.timeNow = str(datetime.date.today().strftime("%d/%m/%Y"))
    
    def getTableRanking(self):
        try:
            with open(self.PATH + '/data_ranking_premier_leaguage.csv','r', encoding="utf-16") as f:
                result = f.readlines()
                result.pop(0)
            table = PrettyTable(["Thứ Hạng","Đội Bóng","Số Trận","Thắng","Hoà","Thua","Bàn Thắng","Bàn Thua","Hiệu Số","Điểm"])
            table.title = "Bảng xếp hạng ngoại hạng Anh ngày " + self.timeNow
            for element in result:
                if element != '\n':
                    row = element.replace('\n', "").split(",")
                    table.add_row([row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]])
            
            return table
        except IOError as ex:
            print("%s" % ex)

if __name__ == "__main__":
    data = RankingPremierLeaguage()
    print(data.getTableRanking())