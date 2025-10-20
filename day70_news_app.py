import requests
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-09-20&sortBy=publishedAt&apiKey=263f05f0505c49729094a2a7fca00ee6"
params = {
    "apiKey": "263f05f0505c49729094a2a7fca00ee6"
}
a = requests.get(url, params=params)
# print(a.text)
# print(a.status_code)
data = a.json()
print(data)
for article in data.get("articles", []):
    print(article.get("title"))
   