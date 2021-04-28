#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue Apr 27 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


from tkinter import *
from tkinter import messagebox as mbox
import copy
import functions as func

__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"


#background color of window, and also listbox. Background color everywhere.
bg_color = '#D9D9D9'


#add/modify a patient dialog
class AddModifyPatientDialog:
	def __init__(self, parent,lst_of_patients,function_update,modify=False):
		top = self.top = Toplevel(parent)
		self.lst_of_patients = lst_of_patients
		#we are passing update_list function as parameter from menu.
		self.function_update = function_update
		#in case user clicks the top right X button to close, call on_closing function
		top.protocol("WM_DELETE_WINDOW", self.on_closing)
		#set background color
		top.configure(background=bg_color)
		#deep copy of list of patients, when modifying we want to modify the copy up until user clicks close.
		#Its only when the user clicks close button we want to reflect the changes on UI and original list.
		#We want to give user option to backtrack by clicking the X on top side of corner to undo changes.
		
		self.lst_of_patients_copy = copy.deepcopy(self.lst_of_patients)
		#when modifying, modifications starts from index 0. Top of the list.
		self.index = 0
		#center dialog on screen, a little bit more height if modifying ( for previous and next buttons). Also set the title whether modify patient or add patient.
		if modify:
			top.title("Modify Patient")
			func.center_window(top,360,150)
		else:
			top.title("Add a Patient")
			func.center_window(top,360,120)
		
		# let us set the add/modify patient screen in a grid
		# first row  with two columns ( name, and textfield to type in)
		lbl_name = Label(top, text="First and Last Name", width=14, anchor='w', bg=bg_color)
		lbl_name.grid(row=0, column=0,padx=(10, 10))	
		self.entry_name_text = StringVar()
		self.name_entry = Entry(top, width = 20,textvariable=self.entry_name_text) 
		self.name_entry.grid(row=0, column=1)

		#second row
		lbl_address = Label(top, text="Address", width=14, anchor='w', bg=bg_color)
		lbl_address.grid(row=1, column=0,padx=(10, 10))
		self.entry_address_text = StringVar()
		self.address_entry = Entry(top, width = 20,textvariable=self.entry_address_text)
		self.address_entry.grid(row=1, column=1)
		
		#third row
		lbl_birthday = Label(top, text="Birthday(mm/dd/yyy)", width=14, anchor='w', bg=bg_color)
		lbl_birthday.grid(row=2, column=0,padx=(10, 10))
		self.entry_birthday_text = StringVar()
		self.birthday_entry = Entry(top, width = 20,textvariable=self.entry_birthday_text)
		self.birthday_entry.grid(row=2, column=1)
		
		#final row for two buttons
		#let us do this in frame ,to fit the two  buttons in the same row/column grid cell.
		self.f1 = Frame(top,bg=bg_color) 
		if modify:
			self.button_save = Button(self.f1, text="Update", width=9, command=self.modify)
		else:
			self.button_save = Button(self.f1, text="Save", width=9, command=self.save)
			
		self.button_close = Button(self.f1, text="Close", width = 9, command=self.close)
		self.button_save.grid(row=0, column=0, pady=(5,5), padx=(10,10))
		self.button_close.grid(row=0, column=1, pady=(5,5), padx=(10,10))
		
		#fit in same row/column two buttons Save/Close together. In case its modify patient fit two buttons Update/Close on 5th row, in case add patient fit two buttons Save/Close on 4th row. 
		#if modify also add prev/next buttons on 4th row this time
		#note rows start from Zero. So 5th row = (row=4)
		if modify:
			self.f1.grid(row=4, column = 1)
			self.f2 = Frame(top,bg=bg_color) 
			self.button_prev = Button(self.f2, text="Prev", width=9, command=self.prev)
			self.button_next = Button(self.f2, text="Next", width = 9, command=self.next)
			self.button_prev.grid(row=0, column=0, pady=(5,5), padx=(10,10))
			self.button_next.grid(row=0, column=1, pady=(5,5), padx=(10,10))
			#fit in same row/column two buttons together
			self.f2.grid(row=3, column = 1)
			self.set_values()
		else:
			self.f1.grid(row=3, column = 1)
		
	#in case user clicked the X button on top side. Notify him that changes he updated will be lost. Instead he should click close button for updated changes to take effect
	def on_closing(self):
		if mbox.askokcancel("Quit", "Are you sure you want to quit? All new or updated changes will be lost?"):
			self.top.destroy()
		
	#modify button clicked, modify in lst_of_patients copy and then when the close button is clicked update initial lst_of_patients and udpate main UI.
	def modify(self):
		self.lst_of_patients_copy[self.index]['name'] = self.name_entry.get()
		self.lst_of_patients_copy[self.index]['address'] = self.address_entry.get()
		self.lst_of_patients_copy[self.index]['birthday'] = self.birthday_entry.get()

	
	#save button clicked, add them to lst_of_patients and update the initial dialog box.
	def save(self):
		json  = { "name": self.name_entry.get(), "address": self.address_entry.get(), "birthday": self.birthday_entry.get()}
		self.lst_of_patients.append(json)
		self.function_update(self.lst_of_patients)
		self.top.destroy()
		
	#in case its modify	, we set the values on screen of patient we are editing.
	def set_values(self):
		self.entry_birthday_text.set(self.lst_of_patients_copy[self.index]['birthday'])
		self.entry_address_text.set(self.lst_of_patients_copy[self.index]['address'])
		self.entry_name_text.set(self.lst_of_patients_copy[self.index]['name'])
	
	#update index, next clicked. and set new values.
	def next(self):
		if self.index < (len(self.lst_of_patients_copy)-1):
			self.index += 1
			self.set_values()
		
	#update index, previous clicked. and set new values.
	def prev(self):
		if self.index > 0:
			self.index -= 1
			self.set_values()
		
	#close the add patient dialog . This is close button clicked.
	#in case modify state, the close button click will update initial list and UI with changes.
	def close(self):
		#in case modify, and we modified like 10 patients. Update initial list. Note this will work always on close button, in case user closes the dialog with 'X' BUTTON on corner I am assuming
		#he cancelled the modifications he did.
		self.lst_of_patients = copy.deepcopy(self.lst_of_patients_copy)
		self.function_update(self.lst_of_patients)
		self.top.destroy()
