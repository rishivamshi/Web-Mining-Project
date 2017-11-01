# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:23:14 2017

@author: rishi
"""

from tkinter import *
import csv
from tables import createStandardTable as cst

window = Tk()

tableFrame = Frame(window, bg='cyan', width=450, height=50, pady=3)
tableFrame2 = Frame(window, bg='gray2', width=50, height=40, padx=3, pady=3)
tableFrame3 = Frame(window, bg = 'red', width = 200, height = 300, padx= 3, pady = 3)

 #tableFrame = Frame(window)

def hideTableFrame():
    tableFrame.grid_forget()


def createTableFrameForFinalList():
    #Your csv file can contain as many rows and colums as needed
    f = open("finallist.csv")
    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()

def createTableFramePriceSortInc():
    #Your csv file can contain as many rows and colums as needed
    f = open("priceSortIncrease.csv")
    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()

def createTableFramePriceSortDec():
    #Your csv file can contain as many rows and colums as needed
    f = open("priceSortDecrease.csv")
    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()
    
def createTableFrameSortDurationDec():
    #Your csv file can contain as many rows and colums as needed
    f = open("sort_durationDec.csv")
    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()

def createTableFrameSortDurationInc():
    #Your csv file can contain as many rows and colums as needed
    f = open("priceSortDecrease.csv")
    #note here I have sent it root but you can also send it a frame
    newtable = cst(f,tableFrame)
    newtable.grid()
    

def ct():
    
    tableFrame.grid()    

def createTableFrame2():
    
    Button(tableFrame2,text="Hide Me",command=hideTableFrame).grid()
    Button(tableFrame2,text="Show me",command=ct).grid()





createTableFrame2()
createTableFrame()
tableFrame3.grid()
tableFrame2.grid()
tableFrame.grid()




window.mainloop()