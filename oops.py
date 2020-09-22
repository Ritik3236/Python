# import pyttsx3
# import requests
#
# engine = pyttsx3.init()
# engine.say("My first code on text-to-speech")

# cls_news = requests.get(
#     'https://newsapi.org/v2/top-headlines?country=in&apiKey=8ce5b726e522439f8626ebb24c2aa4c4'
#     '&category=sport&pageSize=5&q=ipl')

params = input("Enter:> ").split(',')
print(params)
# parsed_news = json.loads(cls_news.text)
# total_news = len(parsed_news['articles'])
# print(total_news)
#
# for i in range(6):
#     title = parsed_news['articles'][i]['title']
#     print(title)
#     engine.say(title)
#     engine.runAndWait()
