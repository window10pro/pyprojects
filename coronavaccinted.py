#data science with python-corona vaccinated news

import bs4
import pandas as pd
import requests

url="https://www.mygov.in/covid-19/"
result=requests.get(url)
soup=bs4.BeautifulSoup(result.content,'html.parser')

news=soup.find_all('div',{"class":"information_row"})
for nw in news:
    print(" corona vaccinated news:",nw.text)
