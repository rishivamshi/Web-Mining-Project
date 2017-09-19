# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 21:13:12 2017

@author: rishi
"""

import timeit
start = timeit.default_timer()




'''
a = input()
b = input()

url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"+a+"_"+b+"_24-09-2017?contains=false&remove="


from selenium import webdriver
chrome_path = r"C:\Python27\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


driver.get(url)


airline_info = driver.find_elements_by_class_name("airline_info_detls")
price = driver.find_elements_by_class_name("num")
for post in airline_info:
    print(post.text)
'''


from tkinter import *
from tkinter import filedialog


def mHello():
    mText=statement.get()
    mlabel1 = Label(myApp,text=mText).pack()

def myNew():
    mlabel1 = Label(myApp,text="YO").pack()

def myOpen():
    myOpen = filedialog.askopenfile()
    mlabel4 = Label(myApp,text=myOpen).pack()

def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        myApp.destroy()
        
    
myApp = Tk()

statement = StringVar()


myApp.geometry('450x450+200+200')

myApp.title('Myapp')

mLabel = Label(myApp,text='my label').pack()

mButton = Button(myApp,text ='OK', command = mHello).pack()


mEntry = Entry(myApp,textvariable=statement).pack()


menubar = Menu(myApp)


filemenu = Menu(menubar, tearoff=0)


filemenu.add_command(label="New", command=myNew)
filemenu.add_command(label="Open", command=myOpen)
filemenu.add_command(label="Save As...")
filemenu.add_command(label="Close", command=mQuit)

menubar.add_cascade(label="File",menu=filemenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help docs")
helpmenu.add_command(label="About",command=mAbout)
menubar.add_cascade(label="Help",menu=helpmenu)




myApp.config(menu=menubar)

myApp.mainloop()

































































        


stop = timeit.default_timer()
print (stop - start )