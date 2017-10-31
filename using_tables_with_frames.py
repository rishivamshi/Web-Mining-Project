from tkinter import *
import csv
from tables import createStandardTable as cst

window = Tk()

tableFrame = Frame(window, bg='cyan', width=450, height=50, pady=3)
tableFrame2 = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)

 #tableFrame = Frame(window)

def hideTableFrame():
    tableFrame.grid_forget()


def createTableFrame():
    #Your csv file can contain as many rows and colums as needed
    f = open("my_csv.csv")

    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()

def ct():
    
    tableFrame.grid()    

def createTableFrame2():
    
    Button(tableFrame2,text="Hide Me",command=hideTableFrame).grid()
    Button(tableFrame2,text="Show me",command=ct).grid()

createTableFrame()
createTableFrame2()
tableFrame.grid()
tableFrame2.grid()



window.mainloop()