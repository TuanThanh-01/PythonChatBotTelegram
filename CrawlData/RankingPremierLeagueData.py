import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class RankingPremierLeaguage:

    def __init__(self):
        ChromeDriverPATH = "../PythonProjectPTIT/etc/chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverPATH)

    def getRankingData(self):
        try:
            self.driver.get("https://vnexpress.net/the-thao/du-lieu-bong-da/giai-dau/premier-league/bang-diem")
            dataRanking = []
            rows = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/div[2]/section/div/div[2]/div[2]/table/tbody/tr"))
            cols = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/div[2]/section/div/div[2]/div[2]/table/tbody/tr[1]/td"))
            for row in range(1, rows+1):
                data = []
                for col in range(1,cols):
                    val = f"/html/body/div[2]/section/div/div[2]/div[2]/table/tbody/tr[{row}]/td[{col}]"
                    data.append(self.driver.find_elements(by=By.XPATH, value=val)[0].text)
                dataRanking.append(data)
            return dataRanking
                
        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()

    def saveDataInFileCSV(self):
        dataRanking = self.getRankingData()
        os.chdir("../PythonProjectPTIT/Data")
        PATH = os.getcwd()
        try:
            with open(PATH + "/data_ranking_premier_leaguage.csv", 'w', encoding="utf-16") as f:
                writer = csv.writer(f)
                writer.writerow(['Thứ Hạng','Đội Bóng','Số Trận','Thắng', 'Hoà','Thua', 'Bàn Thắng', 'Bàn Thua', 'Hiệu Số' ,'Điểm'])
                for data in dataRanking:
                    writer.writerow(data)
        except IOError as ex:
            print("%s" % ex)
            return False

if __name__ == "__main__":
    data = RankingPremierLeaguage()
    data.saveDataInFileCSV()