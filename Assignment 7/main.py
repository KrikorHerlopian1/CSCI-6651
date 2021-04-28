#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue Apr 27 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


from tkinter import *
import menu as menu
import functions as func

__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"


#background color of window, and also listbox. Background color everywhere.
bg_color = '#D9D9D9'
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
#make it global, when patient file opened we want to remove all labels on screen and show listbox instead.
label_lst = []
#this will be the label at start, before user loads new patient file.
label = Label( root, text="Please load patient file", fg='#000000', bg=bg_color)
label_lst.append(label)
label.pack(side=TOP, anchor=NW)

menubar = Menu(root)
root.config(menu=menu.MainMenu(root,menubar,scrollbar,bg_color,label_lst))
#center the window, and initial size 400*300
func.center_window(root,400,300)
#background of the window
root.configure(background=bg_color)
root.title("My Patient Program")
root.mainloop()
