from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import re
import os


""""

full xpath: /html/body/div[2]/div[1]/div
get classes:
+ city, total, daynow, die

"""
class Covid19Data:
    
    def __init__(self, ChromeDriverPATH):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=ChromeDriverPATH)

    def epidemicSituationVN(self):
        # get data
        target = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[1]")
        rawData = target.text.split("\n")
        # handle data(convert list data to dictionaries)
        resDict = {}
        patientIn24h = rawData[2]
        tmpDict = {"TỔNG SỐ CA": rawData[1], patientIn24h[0: 10].upper(): patientIn24h[11:]}
        resDict[rawData[0]] = tmpDict
        resDict[rawData[3]] = rawData[4]
        resDict[rawData[5]] = rawData[6]
        return resDict

    def epidemicSituationWorld(self):
    # get data
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="taben"]'))).click()
        target = self.driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]")
        rawData = target.text.split("\n")
        # handle data(convert list data to dictionaries)
        resDict = {}
        for i in range(0, len(rawData), 2):
            resDict[rawData[i]] = rawData[i + 1]
        return resDict

    def epidemicSituationCity(self):
        target = self.driver.find_elements(by=By.XPATH, value="/html/body/div[2]/div[1]/div")
        for data in target:
            cities = data.find_elements(by=By.CLASS_NAME, value="city")
            totals = data.find_elements(by=By.CLASS_NAME, value="total")
            today = data.find_elements(by=By.CLASS_NAME, value="daynow")
            died = data.find_elements(by=By.CLASS_NAME, value="die")

        list_cities = [city.text for city in cities]
        list_total_patients = [total_patient.text for total_patient in totals]
        list_today_patients = [today_patient.text for today_patient in today]
        list_patients_died = [patient_died.text for patient_died in died]

        resList = []
        for i in range(1, len(list_cities)):
            tmpDict = {
                list_cities[0]: list_cities[i],
                list_total_patients[0]: list_total_patients[i],
                list_today_patients[0]: list_today_patients[i],
                list_patients_died[0]: list_patients_died[i]
            }
            resList.append(tmpDict)
        return resList

    def writeJsonData(self, dct, fileName, path):
        try:
            with open(path + "/" + fileName +".json", 'w', encoding="utf-16") as f:
                json.dump(dct, f, ensure_ascii=False)
        except IOError as ex:
            print("%s" % ex)
            return False

    def getDataCovid19(self):
        os.chdir("../PythonProjectPTIT")
        PATH = os.getcwd() + "/Data"
        try:
            self.driver.get("https://covid19.gov.vn/")
            time.sleep(2)
            self.driver.switch_to.frame(0) # have general data on the epidemic situation of VN and the world
            dataCovidVN = self.epidemicSituationVN()
            dataCovidWorld = self.epidemicSituationWorld()

            self.driver.switch_to.default_content() # return to the parent frame
            self.driver.switch_to.frame(1) # have data on the epidemic situation of the province/city of Vietnam
            dataCovidCityOfVN = self.epidemicSituationCity()

            #save data in file json
            self.writeJsonData(dataCovidVN, "data_covid_vietnam", PATH)
            self.writeJsonData(dataCovidWorld, "data_covid_world", PATH)
            self.writeJsonData(dataCovidCityOfVN, "data_covid_city_vietnam", PATH)
        except Exception as ex:
            print("%s" % ex)
            return False
        finally:
            self.driver.close()

if __name__ == "__main__":
    data = Covid19Data("../PythonProjectPTIT/etc/chromedriver.exe")
    data.getDataCovid19()




