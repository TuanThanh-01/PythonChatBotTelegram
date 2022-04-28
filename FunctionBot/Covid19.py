import os
import json
import datetime
import re
from prettytable import PrettyTable

class Covid19:

      def __init__(self, PATH):
        self.PATH = PATH
      
      def covidVietNam(self):
            try:
                  with open(self.PATH + "/data_covid_vietnam.json", "r", encoding="utf-16") as f:
                        data = json.load(f)
                  
                  table = PrettyTable(["Tổng số ca nhiễm", "Số ca nhiễm 24h qua", "Khỏi", "Tử vong"])
                  table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
                  table.add_row([data['SỐ CA NHIỄM']["TỔNG SỐ CA"], data['SỐ CA NHIỄM']['24 GIỜ QUA'][1:], data['KHỎI'], data["TỬ VONG"]])

                  return table
            except IOError as ex:
                  print("%s" % ex)

      
      def covidWorld(self):
            try:
                  with open(self.PATH + "/data_covid_world.json", "r", encoding="utf-16") as f:
                        data = json.load(f)

                  table = PrettyTable(["Số ca nhiễm", "Khỏi", "Tử vong"])
                  table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
                  table.add_row([data['SỐ CA NHIỄM'], data['KHỎI'], data["TỬ VONG"]])

                  return table
            except IOError as ex:
                  print("%s" % ex)

      def covidAllCityVietNam(self):
            try:
                  with open(self.PATH + "/data_covid_city_vietnam.json", "r", encoding="utf-16") as f:
                        data = json.load(f)
                  
                  table = PrettyTable(['Tỉnh/Thành Phố', "Tổng số ca nhiễm", "Số ca nhiễm 24h qua", "Tử vong"])
                  table.title = "Cập nhật lúc: " + datetime.datetime.now().strftime("%d/%m/%Y")
                  for element in data:
                        table.add_row([element["Tỉnh/TP"], element["Tổng số ca"], element["24 giờ qua"], element["Tử vong"]])
                  
                  return table
            except IOError as ex:
                  print("%s" % ex)

      def no_accent_vietnamese(self, s):
            s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
            s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
            s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
            s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
            s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
            s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
            s = re.sub('[íìỉĩị]', 'i', s)
            s = re.sub('[ÍÌỈĨỊ]', 'I', s)
            s = re.sub('[úùủũụưứừửữự]', 'u', s)
            s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
            s = re.sub('[ýỳỷỹỵ]', 'y', s)
            s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
            s = re.sub('đ', 'd', s)
            s = re.sub('Đ', 'D', s)
            return s

      def covidCityVietNam(self, city):
            try:
                  with open(self.PATH + "/data_covid_city_vietnam.json", "r", encoding="utf-16") as f:
                        listData = json.load(f)
                  
                  result = ""
                  for data in listData:
                        if self.no_accent_vietnamese(data['Tỉnh/TP']).lower() == self.no_accent_vietnamese(city.lower()):
                              result += "🏢 Tỉnh/Thành Phố: " + data['Tỉnh/TP']
                              result += "\n😷 Tổng số ca: " + data['Tổng số ca']
                              result += "\n📈 Số ca nhiễm 24h qua: " + data['24 giờ qua']
                              result += "\n💀 Số ca tử vong: " + data['Tử vong']
                              break
                  return result
            except IOError as ex:
                  print("%s" % ex)
                  
            
            
if __name__ == "__main__":           
      data = Covid19()
      print(data.covidCityVietNam("hai phong"))
