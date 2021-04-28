#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue Apr 27 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================

#main class, Just call Menu class and put a label on screen to load a patient file.
#for menu class make sure to pass label, in order to destroy it when we want to load the list.
# we making sure screen is scrollable, we could have a million patient.


from tkinter import *
import menu as menu
import functions as func

__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"

"""
	You need to run this file to run the application. python3 main.py
"""

#background color of window, and also listbox. Background color everywhere.
bg_color = '#D9D9D9'
root = Tk()
#we need scrolling, we could have one million patients.
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
#When patient file opened we want to remove all labels on screen and show listbox instead. pass this label_lst to menu  to destroy it when loading patients file.
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
