import json

import pyttsx3
import requests

engine = pyttsx3.init()

# country = input("Enter Country code : ")
# # category = input("Enter Category : ")
# news_item = input("Enter News_item : ")
# q = input("Enter Topic : ")
url = 'https://newsapi.org/v2/everything'
params = {'pageSize': 10, 'q': ['Water'], 'sortBy': 'relevancy'}
# params = {'country': 'in', 'category': 'sport', 'pageSize': '5', 'q': 'ipl', 'sortBy': 'relevancy'}

cls_news = requests.get(url, params=params, headers={'X-Api-Key': '8ce5b726e522439f8626ebb24c2aa4c4'})
if cls_news.status_code == 200:
    parsed_news = json.loads(cls_news.text)
    for i in range(len(parsed_news['articles'])):
        try:
            title = parsed_news['articles'][i]['title']
            print(f"{i + 1}. {title}")
            engine.say(title)
            engine.runAndWait()
        except KeyboardInterrupt:
            print("ERROR")
else:
    error = json.loads(cls_news.text)
    print(f"Status Code : {cls_news.status_code}\nError : {error['message']}")
