#data science with python-corona vaccinated news

import bs4
import pandas as pd
import requests

url="https://www.mygov.in/covid-19/"
result=requests.get(url)
soup=bs4.BeautifulSoup(result.content,'html.parser')
news=soup.find_all('div',{"class":"vaccinated-view"})
for nw in news:
    print("corona vaccinated news:",nw.text)
t=nw.text
from tkinter import *
root=Tk()
root.title('corona vaccinated')
root.configure(bg='lightgreen')
t1='india vaccinted'
w1=Label(root,text=t1,bg='blue',font='sans 16')
t2='people vaccinated'
w2=Label(root,text=t2,bg='blue',font='sans 16')
w3=Label(root,text="Corona live Vaccinated News",fg="orange",bg="green",font='sans 16')
w4=Label(root,text=t,fg="black",bg="green",font='sans 16')
w3.pack(fill='both')
w2.pack(fill='both')
w1.pack(fill='both')
w4.pack(fill='both')
root.mainloop()
