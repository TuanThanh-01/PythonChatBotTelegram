from bs4 import BeautifulSoup
import requests as rq

class Article:

    def __init__(self):
        self.url = "https://dantri.com.vn/su-kien.htm"
        response = rq.get(self.url)
        self.soup = BeautifulSoup(response.content, "html.parser")
    
    def getNews(self):
        body_part = self.soup.find('body')
        titles = body_part.find_all("h3", {'class': "article-title"})
        string_url= "https://dantri.com.vn/"
        resData = []
        for title in titles:
            a_tag = title.find("a")

            tmpDict = {}
            tmpDict['title'] = title.text
            tmpDict['url'] = string_url + a_tag['href']
            resData.append(tmpDict)
        
        return resData


if __name__ == "__main__":
    article = Article()
    print(article.getNews())




