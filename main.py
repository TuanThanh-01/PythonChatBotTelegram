from telegram import ParseMode, Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from FunctionBot import Weather
from FunctionBot import Article
from FunctionBot import Image
import random

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Xin chào {update.effective_user.first_name}')
    update.message.reply_text("Sử dụng /help để biết thêm thông tin")
    

def help(update: Update, context: CallbackContext) -> None:
    helpMessage = '''/news: Các tin tức mới trong ngày.\n 
/weather tên_thành_phố: Thời tiết tại các thành phố (ví dụ: "/weather Hà Nội").\n
/petrol: Thông tin giá xăng dầu hôm nay.\n
/gold: Thôn tin giá vàng hôm nay.\n
/covid: Xem tình hình covid của việt nam("/covid viet nam"), thế giới("/covid the gioi"), các tỉnh thành của việt nam("/covid ten_tinh_thanh" ví dụ /covid ha noi xem tình hình covid tại hà nội).\n
/image: Xem ảnh (ví dụ: "/image cat" để xem ảnh mèo)
'''
    update.message.reply_text(helpMessage)
def weather(update: Update, context: CallbackContext) -> None:
    weather = Weather.Weather()
    message_text = update.effective_message.text
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

# xử lý exception không tìm thấy ảnh, kiểm tra kích cỡ file ảnh
def image(update: Update, context: CallbackContext) -> None:
    img = Image.Image()
    message_text = update.effective_message.text
    message_text = message_text.replace("/image", "")
    text = message_text.strip()
    listImages = img.getImage(text)
    image = random.choice(listImages)
    imageUrl = image['url']
    imageAuthor = image['author']
    print(imageUrl)
    update.message.reply_photo(imageUrl)
    update.message.reply_text("Tác giả: " + imageAuthor)

updater = Updater('5296769149:AAGf0fYNN8bNwnhtIR2hPkUNoWCcPejRq8g')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('news', news))
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('image', image))


updater.start_polling()
updater.idle()

