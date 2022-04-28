from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import csv

class PetrolPriceData:

    def __init__(self, ChromeDriverPATH):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverPATH)

    def getPetrolPrice(self):
        try:
            self.driver.get("https://webtygia.com/gia-xang-dau/petrolimex.html")
            price_list        = []
            number_of_rows    = len(self.driver.find_elements(by=By.XPATH, value="/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr"))
            number_of_columns = len(self.driver.find_elements(by=By.XPATH, value="/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/thead/tr/td"))

            for row in range (1, number_of_rows + 1):
                price = []
                # tenHang = driver.find_element_by_xpath("/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr[" + str(hang) + "]/td[1]").text
                for column  in range (1, number_of_columns + 1):            
                    crawlXPath = "/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr[" + str(row) + "]/td[" + str(column) + "]"
                    price.append(self.driver.find_element(by=By.XPATH, value=crawlXPath).text)

                # gia = {'Vung 1' : data[0], 'Vung 2' : data[1]}
                # giaXangDau[tenHang].append(gia)
                price_list.append(price)
            return price_list

        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()

    def saveDataInFileCSV(self):
        dataPetrolPrice = self.getPetrolPrice()
        os.chdir("../PythonProjectPTIT")
        PATH = os.getcwd() + "/Data"
        try:
            with open(PATH + "/data_petrol_price.csv", 'w', encoding="utf-16") as f:
                writer = csv.writer(f)
                writer.writerow(['Sản Phẩm', 'Giá vùng 1', 'Giá vùng 2'])
                for data in dataPetrolPrice:
                    writer.writerow(data)
        except IOError as ex:
            print("%s" % ex)
            return False
        
if __name__ == "__main__":
    data = PetrolPriceData("../PythonProjectPTIT/etc/chromedriver.exe")
    data.saveDataInFileCSV()