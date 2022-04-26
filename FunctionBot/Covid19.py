import os
import json
import datetime
from prettytable import PrettyTable

class Covid19:

      def __init__(self):
            os.chdir("../PythonProjectPTIT/Data")
            self.PATH = os.getcwd()
      
      def covidVietNam(self):
            with open(self.PATH + "/data_covid_vietnam.json", "r", encoding="utf-16") as f:
                 data = json.load(f)
            
            table = PrettyTable(["Tổng số ca nhiễm", "Số ca nhiễm 24h qua", "Khỏi", "Tử vong"])
            table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
            table.add_row([data['SỐ CA NHIỄM']["TỔNG SỐ CA"], data['SỐ CA NHIỄM']['24 GIỜ QUA'][1:], data['KHỎI'], data["TỬ VONG"]])

            return table
      
      def covidWorld(self):
            with open(self.PATH + "/data_covid_world.json", "r", encoding="utf-16") as f:
                  data = json.load(f)

            table = PrettyTable(["Số ca nhiễm", "Khỏi", "Tử vong"])
            table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
            table.add_row([data['SỐ CA NHIỄM'], data['KHỎI'], data["TỬ VONG"]])

            return table

      def covidCityVietNam(self):
            with open(self.PATH + "/data_covid_city_vietnam.json", "r", encoding="utf-16") as f:
                  data = json.load(f)
            
            table = PrettyTable(['Tỉnh/Thành Phố', "Tổng số ca nhiễm", "Số ca nhiễm 24h qua", "Tử vong"])
            table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
            for element in data:
                  table.add_row([element["Tỉnh/TP"], element["Tổng số ca"], element["24 giờ qua"], element["Tử vong"]])
            
            return table
data = Covid19()
print(data.covidVietNam())
print(data.covidWorld())
print(data.covidCityVietNam())
