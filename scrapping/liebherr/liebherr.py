import requests
from bs4 import BeautifulSoup


url = "https://www.liebherr.com/en/usa/latest-news/news-press-releases/news-press-releases.html"
res = requests.get(url)
res.raise_for_status()

print(res.status_code)
soup = BeautifulSoup(res.text, "lxml")

articles = soup.find_all("section", attrs={"class":"news_teaser_module"})
# print(articles)

for article in articles:
    print("TITLE : ", article.a.get_text())
    print("DATE : ", article.h2.previous_sibling.previous_sibling.get_text())
    print("CONTENTS : ", article.h2.find_next_sibling("p").text)