# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:28:40 2017

@author: rishi
"""
import tkinter
# create: 
a = tkinter.Tk()
for i in range(10):
   label = tkinter.Label(a, text=str(i))
   label.grid(column=0, row=i)
a.mainloop()

# remove from screen:
for label in a.grid_slaves():
   if int(label.grid_info()["row"]) > 6:
      label.grid_forget()
a.mainloop()