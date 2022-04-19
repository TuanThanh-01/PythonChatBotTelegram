import requests as rq
from googletrans import Translator
from datetime import date

class Weather:

    def __init__(self):
        self.API_KEY = "d7fbc4c5da58efa35cc62a78c6b2af54"
        self.url = "http://api.openweathermap.org/data/2.5/weather?"

    def transalteText(self, text):
        transaltor = Translator()
        transalted = transaltor.translate(text, src="en", dest="vi")
        return transalted.text

    def getDataWeather(self, city):
        request_url = f"{self.url}q={city}&appid={self.API_KEY}"
        response = rq.get(request_url)
        resData = ""
        if response.status_code == 200:
            data = response.json()
            weather = self.transalteText(data['weather'][0]['description'])
            temperature = round(data["main"]["temp"] - 273.15, 2)
            humidity = data["main"]["humidity"]

            if weather == "Vài mây":
                weather = "Ít mây"
            if weather == "Mây bị hỏng":
                weather = "Trời âm u"
            
            resData += "Thời tiết tại: " + city
            resData += "\nThời tiết ngày: " + str(date.today().strftime("%d/%m/%Y"))
            resData += "\nThời tiết hiện tại: " + str(weather)
            resData += "\nNhiệt Độ: " + str(int(temperature)) + "°C"
            resData += "\nĐộ ẩm: " + str(humidity) + "%"
        else:
            resData += "\nKhông tìm thấy thành phố!!!!"

        return resData

if __name__ == "__main__":
    weather = Weather()
    print(weather.getDataWeather("Ha noi"))