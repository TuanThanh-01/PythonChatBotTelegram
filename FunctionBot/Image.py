from ast import keyword
from pexels_api import API
import requests as rq
import random

class Image:

  def __init__(self):
    self.PEXELS_API_KEY = "563492ad6f9170000100000191026b9fbabe473b9b1de004323f282e"
    
  def getImage(self, keyWordSearch):
    api = API(self.PEXELS_API_KEY)
    api.search(keyWordSearch, page=random.choice(range(0, 5)), results_per_page=10)
    photos = api.get_entries()
    listPicture = []

    for photo in photos:
      tmpDict = {
        'url': photo.medium,
        'author': photo.photographer
      }
      listPicture.append(tmpDict)
    return listPicture
    


if __name__ == "__main__":
  count = 0
  while count < 50:
    data = Image()
    lst = data.getImage("dog")
    image = random.choice(lst)
    print(image['url'], image['author'])
    response = rq.get(image['url'])
    print(response.status_code)
    count += 1

