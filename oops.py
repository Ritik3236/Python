import json

import pyttsx3
import requests

engine = pyttsx3.init()

url = 'https://newsapi.org/v2/top-headlines'
params = {'country': 'in', 'category': 'sport', 'pageSize': '5', 'q': 'ipl'}
cls_news = requests.get(url, params=params, headers={'X-Api-Key': '8ce5b726e522439f8626ebb24c2aa4c4'}, timeout=2)
parsed_news = json.loads(cls_news.text)
total_news = len(parsed_news['articles'])
print(total_news)

for i in range(5):
    try:
        title = parsed_news['articles'][i]['title']
        print(title)
        # engine.say(title)
        # engine.runAndWait()
    except:
        print("good")
