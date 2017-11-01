
"""
Created on Fri Sep 1 21:13:12 2017

@author: rishi , srikar, ishas, devashish, akhil

"""

import timeit
start = timeit.default_timer()
import numpy as np
pr=[]
tim=[]
air=[]
depart=[]
arrival=[]
source=[]
destination=[]
duration=[]
stopage=[]
prgo=[]
timgo=[]
airgo=[]
sourcegp=[]
destgo=[]
flightnumgo=[]
airname=[]
departgo=[]
arrivego=[]
airname=[]
flynum=[]
finalgo=[]
stopage2=[]
final=[]
airname1=[]
flight1=[]
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
        
def price_sort_increase():
    sorted(final,key=lambda x:x[7], reverse=False)   

def price_sort_decrease():
    sorted(final,key=lambda x:x[7], reverse=True)          

def run1():
    mtext1 = fromCity.get()
    mtext2 = toCity.get()
    mtext3 = departDate.get()
    mtext4 = departMonth.get()
    url = "https://flights.makemytrip.com/makemytrip/search/O/O/E/1/0/0/S/V0/"+mtext1+"_"+mtext2+"_"+mtext3+"-"+mtext4+"-2017?contains=false&remove="
    url2= "https://paytm.com/flights/flightSearch/MAA-Chennai/DEL-Delhi/1/0/0/E/2017-"+mtext4+"-"+mtext3
    from selenium import webdriver
    chrome_path = r"C:\Python27\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver2= webdriver.Chrome(chrome_path)
    driver.get(url)
    driver2.get(url2)
    airline_info = driver.find_elements_by_class_name("airline_info_detls")
    price = driver.find_elements_by_class_name("num")
    time = driver.find_elements_by_class_name("time_info")
    for post in price:
        
        price=post.text
        price=price.replace(',','')
        price=int(price)
        pr.append(price)
        
    for post in airline_info:
        airline=post.text
        airline=airline.replace('\n',' ')
        air.append(airline)
        
    for post in time :
        t=post.text
        tim.append(post.text)
    
    conarray=[i+"\n"+j+"\n"+k for i,j,k in zip(tim[::3], tim[1::3],tim[2::3])]
    for element in conarray:
       parts = element.split('\n')
       depart.append(parts[0])
       source.append(parts[1])
       arrival.append(parts[2])
       destination.append(parts[3])
       duration.append(parts[4])
       stopage.append(parts[5])
           
              
    
    for k in range(0,len(pr)):
        final.append([air[k],source[k],depart[k],destination[k],arrival[k],duration[k],stopage[k],pr[k]])
    newlist=sorted(final,key=lambda x:x[8], reverse=True) 
    print(newlist)
    
    
    

    airline_info2 = driver2.find_elements_by_class_name("_3H-S")
    price2 = driver2.find_elements_by_class_name("_2gMo")
    fly=driver2.find_elements_by_class_name("NqXj")
    time2 = driver2.find_elements_by_class_name("vY4t")
    stopgo=driver2.find_elements_by_class_name("_7BOG")
    for post in price2:
        pri=post.text
        pri=pri.replace(',','')
        pri=int(pri)
        prgo.append(pri)
    
    for post in stopgo:
        stopage2.append(post.text)
        
    for post in airline_info2:
        airgo.append(post.text)
        
    for post in time2 :
        timgo.append(post.text)
    
    for post in fly :
        flynum.append(post.text)
    
    airname=airgo[::3]
    departgo=airgo[1::3]
    arrivego=airgo[2::3]
    flightnumgo=flynum[::4]
    flightnumgo = [w.replace(' ', '') for w in flightnumgo]
    sourcego=flynum[1::4]
    destgo=flynum[2::4]
    
    conarray2=[i+" "+j for i,j in zip(airname, flightnumgo)]
    for i in range(0,len(prgo)):
        
      finalgo.append([conarray2[k],sourcego[i], departgo[i],destgo[i],arrivego[i],timgo[i],stopage2[i],prgo[i]])   
      
    print(finalgo)      
    
        

  
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