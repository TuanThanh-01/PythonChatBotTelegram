import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CurrencyData:

    def __init__(self):
        ChromeDriverPATH = "../Python Project/Bot_Telegram/etc/chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverPATH)

    def getCurrencyData(self):
        try:
            self.driver.get("https://www.agribank.com.vn/vn/ty-gia")
            time.sleep(2)
            timeUpdate = self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[3]/div/div[2]/div/div/section/div[2]/section[5]/div[2]/div[1]/div")
            currency = []
            currency.append({"Thời gian cập nhật": timeUpdate.text})
            rows = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/div[1]/div/div[3]/div/div[2]/div/div/section/div[2]/section[5]/div[2]/div[1]/table/tbody/tr"))
            cols = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/div[1]/div/div[3]/div/div[2]/div/div/section/div[2]/section[5]/div[2]/div[1]/table/thead/tr/th"))
            for row in range(1, rows-2):
                data = []
                for col in range(1,cols+1):
                    val = f"/html/body/div[1]/div/div[3]/div/div[2]/div/div/section/div[2]/section[5]/div[2]/div[1]/table/tbody/tr[{row}]/td[{col}]"
                    data.append(self.driver.find_elements(by=By.XPATH, value=val)[0].text)
                tmpDict = {}
                tmpDict['Ngoại tệ'] = data[0]
                tmpDict['Mua tiền mặt'] = data[1]
                tmpDict['Mua chuyển khoản'] = data[2]
                tmpDict['Giá bán'] = data[3]
                currency.append(tmpDict)
            return currency
        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()
    
    def saveCurrencyDataInJson(self):
        currencyData = self.getCurrencyData()
        os.chdir("../Python Project/Bot_Telegram/Data")
        PATH = os.getcwd()
        try:
            with open(PATH + "/data_currency.json", 'w', encoding="utf-16") as f:
                json.dump(currencyData, f, ensure_ascii=False)     
        except IOError as ex:
            print("%s" % ex)
            return False
            
if __name__ == "__main__":
    data = CurrencyData()
    data.saveCurrencyDataInJson()

