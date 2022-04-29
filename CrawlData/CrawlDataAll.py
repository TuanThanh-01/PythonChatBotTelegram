import time
from CrawlData import Covid19Data
from CrawlData import CurrencyData
from CrawlData import GoldPriceData
from CrawlData import PetrolPriceData
from CrawlData import RankingPremierLeagueData
import os
import schedule

class CrawlData:

      def __init__(self):
            os.chdir("../PythonProjectPTIT")
            self.CHROMEDRIVERPATH = os.getcwd() + "/etc/chromedriver.exe"

      def crawlDataCovid(self):
            dataCovid = Covid19Data.Covid19Data(self.CHROMEDRIVERPATH)
            dataCovid.getDataCovid19()

      def crawlDataCurrency(self):
            dataCurrency = CurrencyData.CurrencyData(self.CHROMEDRIVERPATH)
            dataCurrency.saveCurrencyDataInJson()

      def crawlDataGoldPrice(self):
            dataGoldPrice = GoldPriceData.GoldPriceData(self.CHROMEDRIVERPATH)
            dataGoldPrice.saveDataInFileJson()

      def crawlDataPetrolPrice(self):
            dataPetrolPrice = PetrolPriceData.PetrolPriceData(self.CHROMEDRIVERPATH)
            dataPetrolPrice.saveDataInFileCSV()

      def crawlDataRankingPremierLeague(self):
            dataRankingPremierLeague = RankingPremierLeagueData.RankingPremierLeaguage(self.CHROMEDRIVERPATH)
            dataRankingPremierLeague.saveDataInFileCSV()

      def scheduleCrawlData(self):
            schedule.every().day.at("19:00").do(self.crawlDataCovid)
            schedule.every().day.at("09:00").do(self.crawlDataCurrency)
            schedule.every().day.at("09:00").do(self.crawlDataPetrolPrice)
            schedule.every(10).minutes.do(self.crawlDataGoldPrice)
            schedule.every().day.at("19:00").do(self.crawlDataRankingPremierLeague)

      def run(self):
            while True:
                  schedule.run_pending()
                  time.sleep(1)

if __name__ == "__main__":
      data = CrawlData()
      data.scheduleCrawlData()
      data.run()