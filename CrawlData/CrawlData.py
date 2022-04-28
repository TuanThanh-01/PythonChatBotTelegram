import Covid19Data
import CurrencyData
import GoldPriceData
import PetrolPriceData
import RankingPremierLeagueData
import os

os.chdir("../PythonProjectPTIT")
CHROMEDRIVERPATH = os.getcwd() + "/etc/chromedriver.exe"

data = Covid19Data.Covid19Data(CHROMEDRIVERPATH)
data.getDataCovid19()

data1 = CurrencyData.CurrencyData(CHROMEDRIVERPATH)
data1.saveCurrencyDataInJson()

data2 = GoldPriceData.GoldPriceData(CHROMEDRIVERPATH)
data2.saveDataInFileJson()

data3 = PetrolPriceData.PetrolPriceData(CHROMEDRIVERPATH)
data3.saveDataInFileCSV()

data4 = RankingPremierLeagueData.RankingPremierLeaguage(CHROMEDRIVERPATH)
data4.saveDataInFileCSV()


