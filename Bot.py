import os
from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from FunctionBot import Weather
from FunctionBot import Article
from FunctionBot import Image
from FunctionBot import Covid19
from FunctionBot import Currency
from FunctionBot import GoldPrice
from FunctionBot import RankingPremierLeaguage
from FunctionBot import Petrol
from CrawlData import CrawlDataAll
import random
import requests as rq
import os

# os.chdir("pythonprojectptit")
PATHDATA = "/app/Data"

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.first_name}')
    update.message.reply_text("Sử dụng /help để biết thêm thông tin")
    

def help(update: Update, context: CallbackContext) -> None:
    helpMessage = '''/news: Các tin tức mới trong ngày. 
/weather tên_thành_phố: Thời tiết tại các thành phố (ví dụ: "/weather Hà Nội").
/petrol: Thông tin giá xăng dầu hôm nay.
/gold: Thông tin giá vàng hôm nay.
/covid: Xem tình hình covid của việt nam("/covid viet nam"), thế giới("/covid the gioi"), các tỉnh thành của việt nam("/covid ten_tinh_thanh" ví dụ /covid ha noi xem tình hình covid tại hà nội).
/image: Xem ảnh (ví dụ: "/image cat" để xem ảnh mèo).
/currency: Xem giá tiền tệ hôm nay.
/ranking: Xem bảng xếp hạng Premier Leaguage.
'''
    update.message.reply_text(helpMessage)


def weather(update: Update, context: CallbackContext) -> None:
    weather = Weather.Weather()
    message_text = update.effective_message.text
    lst = message_text.split()
    message_text = message_text.replace("/weather", "")
    city = message_text.strip()
    update.message.reply_text(weather.getDataWeather(city))

def news(update: Update, context: CallbackContext) -> None:
    news = Article.Article()
    data = news.getNews()
    resString = ""
    for item in data:
        tmpString = item['title'].strip()
        tmpString += "\n" + "Link: " + item['url']
        resString += tmpString +"\n\n"
    update.message.reply_text(resString)

def image(update: Update, context: CallbackContext) -> None:
    img = Image.Image()
    message_text = update.effective_message.text
    message_text = message_text.replace("/image", "")
    text = message_text.strip()
    listImages = img.getImage(text)
    if len(listImages) != 0:
        while True:
            image = random.choice(listImages)
            imageUrl = image['url']
            imageAuthor = image['author']
            response = rq.get(imageUrl)
            if response.status_code == 200:
                break
        update.message.reply_photo(imageUrl)
        update.message.reply_text("Tác giả: " + imageAuthor)
    else:
        update.message.reply_text("Không tìm thấy ảnh!!!")

def currency(update: Update, context: CallbackContext) -> None:
    currencyTable = Currency.Currency(PATHDATA).readFileJson()
    update.message.reply_text(f'<pre>{currencyTable}</pre>', parse_mode=ParseMode.HTML)

def gold(update: Update, context: CallbackContext) -> None:
    goldTable = GoldPrice.GoldPrice(PATHDATA).readFileJson()
    update.message.reply_text(f'<pre>{goldTable}</pre>', parse_mode=ParseMode.HTML)

def petrol(update: Update, context: CallbackContext) -> None:
    petrolTable = Petrol.Petrol(PATHDATA).getTablePetrolPrice()
    update.message.reply_text(f'<pre>{petrolTable}</pre>', parse_mode=ParseMode.HTML)

def ranking(update: Update, context: CallbackContext) -> None:
    rankingTable = RankingPremierLeaguage.RankingPremierLeaguage(PATHDATA).getTableRanking()
    update.message.reply_text(f'<pre>{rankingTable}</pre>', parse_mode=ParseMode.HTML)

def covid(update: Update, context: CallbackContext) -> None:
    message_text = update.effective_message.text
    message_text = message_text.replace("/covid", "")
    text = message_text.strip()
    covid19Data = Covid19.Covid19(PATHDATA)
    if text == "viet nam":
        tableCovid19VietNam = covid19Data.covidVietNam()
        update.message.reply_text(f'<pre>{tableCovid19VietNam}</pre>', parse_mode=ParseMode.HTML)
    elif text == "the gioi":
        tableCovid19TheGioi = covid19Data.covidWorld()
        update.message.reply_text(f'<pre>{tableCovid19TheGioi}</pre>', parse_mode=ParseMode.HTML)
    else:
        try:
            update.message.reply_text(covid19Data.covidCityVietNam(text))
        except:
            update.message.reply_text("Không tìm thấy tên thành phố!!!!")

updater = Updater('5296769149:AAGf0fYNN8bNwnhtIR2hPkUNoWCcPejRq8g')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('image', image))
updater.dispatcher.add_handler(CommandHandler('currency', currency))
updater.dispatcher.add_handler(CommandHandler('gold', gold))
updater.dispatcher.add_handler(CommandHandler('petrol', petrol))
updater.dispatcher.add_handler(CommandHandler('ranking', ranking))
updater.dispatcher.add_handler(CommandHandler('covid', covid))

updater.start_polling()

crawlData = CrawlDataAll.CrawlData()
crawlData.scheduleCrawlData()
crawlData.run()

updater.idle()

