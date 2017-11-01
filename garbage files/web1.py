
"""
Created on Fri Sep 1 21:13:12 2017

@author: rishi , srikar, ishas, devashish, akhil

"""

import timeit
start = timeit.default_timer()


from tkinter import *
from tkinter import filedialog

# Functions
def inputFrom():
    mText=fromCity.get()
    mlabel1 = Label(WM,text=mText).pack()
def inputTo():
    mText=toCity.get()
    mlabel1 = Label(WM,text=mText).pack()
def inputDepDate():
    mText=departDate.get()
    mlabel1 = Label(WM,text=mText).pack()

def inputDepMon():
    mText=departMonth.get()
    mlabel1 = Label(WM,text=mText).pack()

def myNew():
    mlabel1 = Label(WM,text="YO").pack()

def myOpen():
    myOpen = filedialog.askopenfile()
    mlabel4 = Label(WM,text=myOpen).pack()

def mAbout():
    messagebox.showinfo(title="About",message="This is the about box")

def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Are you sure")
    if mExit > 0:
        WM.destroy()

def run1():
    mtext1 = fromCity.get()
    mtext2 = toCity.get()
    mtext3 = departDate.get()
    mtext4 = departMonth.get()
    url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"+mtext1+"_"+mtext2+"_"+mtext3+"-"+mtext4+"-2017?contains=false&remove="

    from selenium import webdriver
    chrome_path = r"C:\Python27\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)

    driver.get(url)

    airline_info = driver.find_elements_by_class_name("airline_info_detls")
    price = driver.find_elements_by_class_name("num")
    time = driver.find_elements_by_class_name("time_info")
    for post in price:
        print(post.text)
    for post in airline_info:
        print(post.text)
    for post in time :
        print(post.text)



  
WM = Tk()

fromCity = StringVar()
toCity = StringVar()
departDate = StringVar()
departMonth = StringVar()

### WM object - Labels, Inputs for - From, To, Date, Month and Run
WM.geometry('450x450+200+200')

WM.title('Web Mining - WEB SCRAPING FOR MAKE-MY-TRIP')

mLabel1 = Label(WM,text='FROM').pack()
mButton1 = Button(WM,text ='OK', command = inputFrom).pack()
mEntry1 = Entry(WM,textvariable=fromCity).pack()


mLabel2 = Label(WM,text='TO').pack()
mButton2 = Button(WM,text ='OK', command = inputTo).pack()
mEntry2 = Entry(WM,textvariable=toCity).pack()


mLabel3 = Label(WM,text='DATE').pack()
mButton3 = Button(WM,text ='OK', command = inputDepDate).pack()
mEntry3 = Entry(WM,textvariable=departDate).pack()

mLabel4 = Label(WM,text='MONTH').pack()
mButton4 = Button(WM,text ='OK', command = inputDepMon).pack()
mEntry4 = Entry(WM,textvariable=departMonth).pack()

mRun = Button(WM,text ='RUN', command = run1).pack()

# MenuBar - FOR FUN
menubar = Menu(WM)

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

WM.config(menu=menubar)
# MenuBar - Ended

WM.mainloop()

stop = timeit.default_timer()
print (stop - start )