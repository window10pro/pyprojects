#data science with python-google live news

import bs4
import pandas as pd
import requests

url="https://timesofindia.indiatimes.com/india/breaking-news-live-updates-12-08-2021/liveblog/85259676.cms"

result=requests.get(url)
soup=bs4.BeautifulSoup(result.content,'html.parser')


news=soup.find_all('div',{"class":"_39vwh rel"})
for nw in news:
    print("google news:",nw.text)
