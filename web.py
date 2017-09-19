# -*- coding: utf-8 -*-
"""
Created on Sun Sep 1 21:13:12 2017

@author: rishi , srikar, ishas, devashish, akhil
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
for post in price:
    print(post.text)

'''

from tkinter import *
from tkinter import filedialog


def mHello():
    mText=statement1.get()
    mlabel1 = Label(myApp,text=mText).pack()
def mHello1():
    mText=statement2.get()
    mlabel1 = Label(myApp,text=mText).pack()
def mHello2():
    mText=statement3.get()
    mlabel1 = Label(myApp,text=mText).pack()

def mHello3():
    mText=statement4.get()
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


def run1():
    mtext1 = statement1.get()
    mtext2 = statement2.get()
    mtext3 = statement3.get()
    mtext4 = statement4.get()
    url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"+mtext1+"_"+mtext2+"_"+mtext3+"-"+mtext4+"-2017?contains=false&remove="


    from selenium import webdriver
    chrome_path = r"C:\Python27\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)


    driver.get(url)


    #airline_info = driver.find_elements_by_class_name("airline_info_detls")
    price = driver.find_elements_by_class_name("num")
    for post in price:
        print(post.text)




























       
    
myApp = Tk()

statement1 = StringVar()
statement2 = StringVar()
statement3 = StringVar()
statement4 = StringVar()

myApp.geometry('450x450+200+200')

myApp.title('Myapp')

mLabel1 = Label(myApp,text='FROM').pack()
mButton1 = Button(myApp,text ='OK', command = mHello).pack()
mEntry1 = Entry(myApp,textvariable=statement1).pack()


mLabel2 = Label(myApp,text='TO').pack()
mButton2 = Button(myApp,text ='OK', command = mHello1).pack()
mEntry2 = Entry(myApp,textvariable=statement2).pack()


mLabel3 = Label(myApp,text='TO').pack()
mButton3 = Button(myApp,text ='OK', command = mHello2).pack()
mEntry3 = Entry(myApp,textvariable=statement3).pack()

mLabel4 = Label(myApp,text='TO').pack()
mButton4 = Button(myApp,text ='OK', command = mHello3).pack()
mEntry4 = Entry(myApp,textvariable=statement4).pack()




mButton2 = Button(myApp,text ='RUN', command = run1).pack()






















# MenuBar - FOR FUN
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