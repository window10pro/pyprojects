import bs4
import pandas as pd
import requests
from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()
root.geometry('600x300+0+0')
root.title('Trending News Application')
root.configure(bg='white')

#root.state('zoomed')
lb=tk.Label(root, text='Trending News Application',font='sans 14',bg='#8207f5', fg='white').pack(fill='both')
lb3=tk.Label(root, text='Its a Data Science Application',font='sans 14',bg='#f0f288', fg='blue').pack(fill='both')

img1=ImageTk.PhotoImage(Image.open("news.jpg"))
lb=Label(root,image=img1).pack()


def gennews():
    import gen_news as gn
b3=tk.Button(root, text='Trending All News', command=gennews,bg='blue', fg='white', font='sans 14',height=2, width=25).pack()
img2=ImageTk.PhotoImage(Image.open("news1.jpg"))
lb=Label(root,image=img2).pack()



def sports():
    import sportsnews as sp
b4=tk.Button(root, text='Trending Sports News', command=sports,bg='green', fg='white', font='sans 14',height=2, width=25).pack()
img3=ImageTk.PhotoImage(Image.open("snews1.jpg"))
lb=Label(root,image=img3).pack()


def entertainment():
    import entertainmentnews as en
b5=tk.Button(root, text='Trending Enterianment News', command=entertainment,bg='purple', fg='white', font='sans 14',height=2, width=25).pack()
img4=ImageTk.PhotoImage(Image.open("enews.jpg"))
lb=Label(root,image=img4).pack()



def movies():
    import movies_news as mv
b6=tk.Button(root, text='Trending Movies News', command=movies,bg='pink', fg='blue', font='sans 14',height=2, width=25).pack()
img5=ImageTk.PhotoImage(Image.open("smovie.jpg"))
lb=Label(root,image=img5).pack()


b6=tk.Button(root, text='Close Application', command=root.destroy,bg='red', fg='white',font='sans 14',height=2, width=25).pack()
lb2=tk.Label(root, text='BCA final year',font='sans 14',bg='green', fg='white').pack(fill='both', side=tk.BOTTOM)
