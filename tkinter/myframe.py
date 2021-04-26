#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Mon Apr 26 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


import tkinter as tk
import sys
from tkinter import messagebox as mbox

class MyFrame(tk.Frame):
	def onClick(self):
		mbox.showinfo("Button clicked", "Button clicked")	
	def __init__(self, parent):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Hello, world")
		button = tk.Button(self,compound = "center",text="button",command = self.onClick)
		
		label.pack()
		button.pack()
		label.bind("<1>", lambda e: self.quit())
		
		def quit(self, event=None):
			sys.exit(0)
			
	
				
			
			
root = tk.Tk()
root.geometry('200x150')
MyFrame(root).pack()
root.mainloop()

