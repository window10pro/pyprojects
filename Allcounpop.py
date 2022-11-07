import bs4
import pandas as pd
import requests
from tkinter import ttk
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
root = Tk()

Title=root.title
root.geometry("1500x900")

lb=tk.Label(root, text='POPULATIONS NEWS',font='sans 14',bg='#8207f5', fg='gold')

lb3=tk.Label(root, text='Its a Data Science Application',font='sans 14',bg='#f0f288', fg='blue')


img=ImageTk.PhotoImage(Image.open("news.jpg"))
lb=Label(root,image=img).pack()


def brazil():
    import brazilpop as br
b1=tk.Button(root, text='Brazil Populations  News', command=brazil ,bg='orange', fg='black', font='sans 14',height=2, width=25).pack()

def northkorea():
    import northpop as nk
b2=tk.Button(root, text='North Populations  News', command=northkorea ,bg='white', fg='brown', font='sans 14',height=2, width=25).pack()

def dubai():
    import dubaipop as nk
b3=tk.Button(root, text='Dubai populations  News', command=dubai ,bg='green', fg='brown', font='sans 14',height=2, width=25).pack()

def india():
    import indiapop_news as id
b4=tk.Button(root, text='India populations News', command=india ,bg='red', fg='green', font='sans 14',height=2, width=25).pack()


def andaman():
    import andamanpop as an
b5=tk.Button(root, text=' Andaman populations News', command=andaman,bg='gold', fg='green', font='sans 14',height=2, width=25).pack()


b6=tk.Button(root, text='Remove Application', command=root.destroy,bg='brown', fg='yellow',font='sans 14',height=2, width=25).pack()
lb2=tk.Label(root, text='asian country populations',font='sans 14',bg='green', fg='white') 


