import Covid19Data
import CurrencyData
import GoldPriceData
import PetrolPriceData
import RankingPremierLeaguageData


data = Covid19Data.Covid19Data()
data.getDataCovid19()

data1 = CurrencyData.CurrencyData()
data1.saveCurrencyDataInJson()

data2 = GoldPriceData.GoldPriceData()
data2.saveDataInFileJson()

data3 = PetrolPriceData.PetrolPriceData()
data3.saveDataInFileCSV()

data4 = RankingPremierLeaguageData.RankingPremierLeaguage()
data4.saveDataInFileCSV()


