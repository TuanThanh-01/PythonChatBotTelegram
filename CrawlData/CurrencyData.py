import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CurrencyData:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

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
        # os.chdir("pythonprojectptit")
        PATH = "/app/Data"
        try:
            with open(PATH + "/data_currency.json", 'w', encoding="utf-16") as f:
                json.dump(currencyData, f, ensure_ascii=False)     
        except IOError as ex:
            print("%s" % ex)
            return False
            
# if __name__ == "__main__":
#     data = CurrencyData("app/etc/chromedriver.exe")
#     data.saveCurrencyDataInJson()

