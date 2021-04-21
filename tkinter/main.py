#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed Apr 14 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================
import tkinter
import tkinter.messagebox
from tkinter import *
def helloCallBack():
	tkinter.messagebox.showinfo("Hello Python","Hello Krikor")
top = tkinter.Tk()
B = tkinter.Canvas(top, bg ="#FFF000",width=500)
#coord = 20, 45, 20, 200 
#B.create_line(coord)
#coord = 10, 50, 120, 180 
#B.create_arc(coord, start=0, extent=90, fill="pink")
#B.create_arc(coord, start=80, extent=90, fill="pink")
#B.create_arc(coord, start=160, extent=90, fill="pink")
#B.create_arc(coord, start=260, extent=90, fill="pink")

button = tkinter.Button( text="Hello",bg="blue" ,command = helloCallBack)
button.place(relx=0.5, rely=0.5, anchor=CENTER)
#button.pack()
B.pack()

top.mainloop()

