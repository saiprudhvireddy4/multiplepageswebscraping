import requests
from bs4 import BeautifulSoup
import pandas as pd




books = []

for i in range(1,5):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    req = requests.get(url)
    req.raise_for_status()
    soup = BeautifulSoup(req.content, "html.parser")
    ol= soup.find("ol")
    articles=ol.find_all("article",class_="product_pod")
    for article in articles:
        image = article.find("img")
        title = image.attrs["alt"]
        star = article.find("p")
        star=star["class"][1]
        price = article.find("p",class_="price_color").text
        price= float(price[1:])
        books.append([title,price,star])

df = pd.DataFrame(books,columns=["Title","price","Star Rating"])
df.to_csv("books.csv")
