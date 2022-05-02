from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import csv

class PetrolPriceData:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    def getPetrolPrice(self):
        try:
            self.driver.get("https://webtygia.com/gia-xang-dau/petrolimex.html")
            price_list        = []
            number_of_rows    = len(self.driver.find_elements(by=By.XPATH, value="/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr"))
            number_of_columns = len(self.driver.find_elements(by=By.XPATH, value="/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/thead/tr/td"))

            for row in range (1, number_of_rows + 1):
                price = []
                for column  in range (1, number_of_columns + 1):            
                    crawlXPath = "/html/body/main/div[5]/div/div[2]/div/div/div/div[1]/div[2]/table/tbody/tr[" + str(row) + "]/td[" + str(column) + "]"
                    price.append(self.driver.find_element(by=By.XPATH, value=crawlXPath).text)

                price_list.append(price)
            return price_list

        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()

    def saveDataInFileCSV(self):
        dataPetrolPrice = self.getPetrolPrice()
        # os.chdir("pythonprojectptit")
        PATH = "/app/Data"
        try:
            with open(PATH + "/data_petrol_price.csv", 'w', encoding="utf-16") as f:
                writer = csv.writer(f)
                writer.writerow(['Sản Phẩm', 'Giá vùng 1', 'Giá vùng 2'])
                for data in dataPetrolPrice:
                    writer.writerow(data)
        except IOError as ex:
            print("%s" % ex)
            return False
        
# if __name__ == "__main__":
#     data = PetrolPriceData("pythonprojectptit/etc/chromedriver.exe")
#     data.saveDataInFileCSV()