import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


class GoldPriceData:

    def __init__(self):
        ChromeDriverPATH = "../PythonProjectPTIT/etc/chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverPATH)


    def getGoldPrice(self):
        try:
            self.driver.get("https://dantri.com.vn/gia-vang.htm")
            time.sleep(2)
            timeUpdate = self.driver.find_element(by=By.XPATH, value="/html/body/main/div[2]/div[2]/b").text
            data = []
            data.append({"Thời gian cập nhật": timeUpdate})
            rows = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/main/div[3]/div[1]/div[1]/div/section/table/tbody/tr"))
            cols = len(self.driver.find_elements(by=By.XPATH,value= "/html/body/main/div[3]/div[1]/div[1]/div/section/table/tbody/tr[1]/td"))
            for row in range(1, rows):
                # the table doesn't contain row 5, row 10
                if row == 5 or row == 10:
                    continue
                else:
                    goldType = ''
                    purchasePrice = ''
                    salePrice = ''
                    purchaseCompareYesterday = ''
                    saleComapreYesterday = ''
                    for col in range(2, cols + 1):
                        val = f"/html/body/main/div[3]/div[1]/div[1]/div/section/table/tbody/tr[{row}]/td[{col}]/span"
                        if col == 2:
                            goldType = self.driver.find_elements(by=By.XPATH, value=val)[0].text
                        elif col == 3:
                            # because span tag splits into a list -> get element in this list 
                            # check len of list if len > 1 -> it has compare price yesterday
                            if len(self.driver.find_elements(by=By.XPATH, value=val)) > 1:
                                span1 = val + "[1]"
                                span2 = val + "[2]"
                                purchasePrice = self.driver.find_elements(by=By.XPATH, value=span1)[0].text
                                purchaseCompareYesterday = self.driver.find_elements(by=By.XPATH, value=span2)[0].text
                                getClass = self.driver.find_elements(by=By.XPATH, value=span2)[0].get_attribute("class")
                                if 'down' in getClass:
                                    purchaseCompareYesterday = "Giảm " + purchaseCompareYesterday
                                elif 'up' in getClass:
                                    purchaseCompareYesterday = "Tăng " + purchaseCompareYesterday
                            else:
                                purchasePrice = self.driver.find_elements(by=By.XPATH, value=val)[0].text
                        
                        elif col == 4:
                            if len(self.driver.find_elements(by=By.XPATH, value=val)) > 1:
                                span1 = val + "[1]"
                                span2 = val + "[2]"
                                salePrice = self.driver.find_elements(by=By.XPATH, value=span1)[0].text
                                saleComapreYesterday = self.driver.find_elements(by=By.XPATH, value=span2)[0].text
                                getClass = self.driver.find_elements(by=By.XPATH, value=span2)[0].get_attribute("class")
                                if 'down' in getClass:
                                    saleComapreYesterday = "Giảm " + saleComapreYesterday
                                elif 'up' in getClass:
                                    saleComapreYesterday = "Tăng " + saleComapreYesterday
                            else:
                                salePrice = self.driver.find_elements(by=By.XPATH, value=val)[0].text
                    tmpDict = {}
                    tmpDict['Loại vàng'] = goldType
                    tmpDict['Giá mua'] = purchasePrice + " " + purchaseCompareYesterday
                    tmpDict['Giá bán'] = salePrice + " " + saleComapreYesterday
                    data.append(tmpDict)
            return data
        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()

    def saveDataInFileJson(self):
        dataGoldPrice = self.getGoldPrice()
        os.chdir("../PythonProjectPTIT/Data")
        PATH = os.getcwd()
        try:
            with open(PATH + "/data_gold_price.json", 'w', encoding="utf-16") as f:
                json.dump(dataGoldPrice, f, ensure_ascii=False)
        except IOError as ex:
            print("%s" % ex)
            return False
if __name__ == "__main__":
    data = GoldPriceData()
    data.saveDataInFileJson()
        




