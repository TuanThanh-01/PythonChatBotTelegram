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
            self.CHROMEDRIVERPATH = "/app/etc/chromedriver.exe"

      def crawlDataCovid(self):
            dataCovid = Covid19Data.Covid19Data()
            dataCovid.getDataCovid19()

      def crawlDataCurrency(self):
            dataCurrency = CurrencyData.CurrencyData()
            dataCurrency.saveCurrencyDataInJson()

      def crawlDataGoldPrice(self):
            dataGoldPrice = GoldPriceData.GoldPriceData()
            dataGoldPrice.saveDataInFileJson()

      def crawlDataPetrolPrice(self):
            dataPetrolPrice = PetrolPriceData.PetrolPriceData()
            dataPetrolPrice.saveDataInFileCSV()

      def crawlDataRankingPremierLeague(self):
            dataRankingPremierLeague = RankingPremierLeagueData.RankingPremierLeaguage()
            dataRankingPremierLeague.saveDataInFileCSV()

      def scheduleCrawlData(self):
            schedule.every(15).minutes.do(self.crawlDataCovid)
            schedule.every(15).minutes.do(self.crawlDataCurrency)
            schedule.every(15).minutes.do(self.crawlDataPetrolPrice)
            schedule.every(15).minutes.do(self.crawlDataGoldPrice)
            schedule.every(15).minutes.do(self.crawlDataRankingPremierLeague)

      def run(self):
            while True:
                  schedule.run_pending()
                  time.sleep(1)

# if __name__ == "__main__":
#       data = CrawlData()
#       data.scheduleCrawlData()
#       data.run()