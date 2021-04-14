#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed Apr 14 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================
import tkinter

top = tkinter.Tk()
B = tkinter.Canvas(top, bg ="#FFF000",width=500)
coord = 20, 45, 20, 200 
B.create_line(coord)
B.pack()
top.mainloop()

