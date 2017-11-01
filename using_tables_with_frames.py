from tkinter import *
import csv
from tables import createStandardTable as cst

window = Tk()

tableFrame = Frame(window, bg='cyan', width=450, height=50, pady=3)
tableFrame2 = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
tableFrame3 = Frame(window, bg = 'red', width = 200, height = 300, padx= 3, pady = 3)


def tableFrames():
    tableFrame3.grid()
    tableFrame2.grid()
    tableFrame.grid()
    
    

 #tableFrame = Frame(window)
f = open("my_csv.csv")
newtable = cst(f,tableFrame)




def createTableFrame():
    #Your csv file can contain as many rows and colums as needed
    f = open("sort_durationDec.csv")

    #note here I have sent it root but you can also send it a frame
    global newtable
    newtable = cst(f,tableFrame)
    newtable.grid()

def createTableFrame3():
    #Your csv file can contain as many rows and colums as needed
    f = open("priceSortIncrease.csv")

    #note here I have sent it root but you can also send it a frame
    global newtable
    newtable = cst(f,tableFrame)
    newtable.grid()
def createTableFrame4():
    #Your csv file can contain as many rows and colums as needed
    f = open("priceSortDecrease.csv")

    #note here I have sent it root but you can also send it a frame
    global newtable
    newtable = cst(f,tableFrame)
    newtable.grid()
def createTableFrame5():
    #Your csv file can contain as many rows and colums as needed
    f = open("sort_durationInc.csv")

    #note here I have sent it root but you can also send it a frame
    global newtable
    newtable = cst(f,tableFrame)
    newtable.grid()




def ct():
    global newtable
    newtable.destroy()
    createTableFrame3()
    tableFrame.grid()    
def th():
    global newtable
    newtable.destroy()
    createTableFrame()
    tableFrame.grid()
def t2h():
    global newtable
    newtable.destroy()
    createTableFrame4()
    tableFrame.grid()

def t3h():
    global newtable
    newtable.destroy()
    createTableFrame5()
    tableFrame.grid()


def createTableFrame2():
    
    Button(tableFrame2,text="Hide Me",command=hideTableFrame).grid()
    Button(tableFrame2,text="Show Price Sort Increase",command=ct).grid()
    Button(tableFrame2,text = "Show Sort Duration Decreate", command = th).grid()
    Button(tableFrame2,text = "Show Price Sort Decrease", command = t2h).grid()
    Button(tableFrame2,text = "Show Sort Duration Increase", command = t3h).grid()

def inputs():
    mLabel1 = Label(WM,text='FROM')
    mButton1 = Button(WM,text ='OK', command = inputFrom)
    mEntry1 = Entry(WM,textvariable=fromCity)


    mLabel2 = Label(WM,text='TO')
    mButton2 = Button(WM,text ='OK', command = inputTo)
    mEntry2 = Entry(WM,textvariable=toCity)


    mLabel3 = Label(WM,text='DATE')
    mButton3 = Button(WM,text ='OK', command = inputDepDate)
    mEntry3 = Entry(WM,textvariable=departDate)

    mLabel4 = Label(WM,text='MONTH').pack()
    mButton4 = Button(WM,text ='OK', command = inputDepMon)
    mEntry4 = Entry(WM,textvariable=departMonth)

    mRun = Button(WM,text ='RUN', command = run1)


tableFrames()
createTableFrame2()
createTableFrame3()
#createTableFrame()







window.mainloop()