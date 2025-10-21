import requests
import json
query = input("What kind of news you want: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-09-20&sortBy=publishedAt&apiKey=263f05f0505c49729094a2a7fca00ee6"
# params = {
#     "apiKey": "263f05f0505c49729094a2a7fca00ee6"
# }
# a = requests.get(url, params=params)
# # print(a.text)
# # print(a.status_code)
# data = a.json()
# print(data)
# for article in data.get("articles", []):
#     print(article.get("title"))
r= requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------")
    