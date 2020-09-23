import json

import pyttsx3
import requests

engine = pyttsx3.init()

# country = input("Enter Country code : ")
# # category = input("Enter Category : ")
# news_item = input("Enter News_item : ")
# q = input("Enter Topic : ")
url = 'https://newsapi.org/v2/everything'

# params = {'pageSize': 5, 'q': 'ipl', 'sortBy': 'relevancy'}
params = {'country': 'in', 'category': 'sport', 'pageSize': '5', 'q': 'ipl', 'sortBy': 'relevancy'}

cls_news = requests.get(url, params=params, headers={'X-Api-Key': '8ce5b726e522439f8626ebb24c2aa4c4'})
var = cls_news.status_code
if var == 200:
    parsed_news = json.loads(cls_news.text)
    print(parsed_news)

    for i in range(len(parsed_news['articles'])):
        try:
            title = parsed_news['articles'][i]['title']
            print(title)
            # engine.say(title)
            # engine.runAndWait()
        except:
            print("good")
else:
    error = json.loads(cls_news.text)
    print(error['code'], error['message'])
