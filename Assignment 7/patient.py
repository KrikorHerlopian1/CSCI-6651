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

# Add or Modify patient dialog here

#background color of window, and also listbox. Background color everywhere.
bg_color = '#D9D9D9'


#add/modify a patient dialog
class AddModifyPatientDialog:
	def __init__(self, parent,lst_of_patients,function_update,modify=False):
		"""
			let us create the form in dialog here. Whether modify or add. 
		"""
		top = self.top = Toplevel(parent)
		self.lst_of_patients = lst_of_patients
		#we are passing update_list function from menu class as parameter here.
		self.function_update = function_update
		#in case user clicks the top right X button to close, call on_closing function
		top.protocol("WM_DELETE_WINDOW", self.on_closing)
		#set background color
		top.configure(background=bg_color)
		#deep copy of list of patients, when modifying we want to modify the copy up until user clicks save all.
		#Its only when the user clicks save all button we want to reflect the changes on UI and original list.
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
			self.button_save = Button(self.f1, text="Update", width=9, command=self.modify_patient)
			self.button_close = Button(self.f1, text="SaveAll", width = 9, command=self.save_all)
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
		
	#in case user clicked the X button on top side. Notify him that changes he updated will be lost. Instead he should click save all button for updated changes to take effect
	def on_closing(self):
		if mbox.askokcancel("Quit", "Are you sure you want to quit? All new or updated changes will be lost?"):
			self.top.destroy()
		
	#modify button clicked
	def modify_patient(self):
		#validate form first, before proceeding to updating the current patient open on screen
		if self.validate_form():
			self.modify()
	
	#modify in lst_of_patients copy and then when the save all button is clicked update initial lst_of_patients and udpate main UI.
	def modify(self):
		self.lst_of_patients_copy[self.index]['name'] = self.name_entry.get()
		self.lst_of_patients_copy[self.index]['address'] = self.address_entry.get()
		self.lst_of_patients_copy[self.index]['birthday'] = self.birthday_entry.get()

	def validate_form(self):
		"""
			Male sure a name , address, and birthday are typed. in case of birthday make sure date is correct format.
		"""
		message = ''
		if self.name_entry.get() == '':
			message += 'Name cannot be empty\n'
		if self.address_entry.get() == '':
			message += 'Address cannot be empty\n'
		if self.birthday_entry.get() == '':
			message += 'Birthday cannot be empty\n'
		elif not func.valid_date(self.birthday_entry.get()):
			message += 'Birthday not valid\n'
		if message:
			#show popup of errors that need to be fixed
			mbox.showinfo("Error", message)
			return False
			
		return True
	    		
	#save button clicked, add them to lst_of_patients and update the initial dialog box.
	def save(self):
		#validate form first, before proceeding to saving the new patient open on screen and closing the box + updating UI.
		if self.validate_form():
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
			#Let us give user notice in case modifications not saved
			if self.check_if_modified():
				if mbox.askokcancel("Warning", "Do you want save changes before moving?"):
					#validate form first, before proceeding to modifying the current patient open on screen and moving to next patient
					if self.validate_form():
						self.modify()
					else:
						return
			self.index += 1
			self.set_values()
		
	#update index, previous clicked. and set new values.
	def prev(self):
		if self.index > 0:
			#Let us give user notice in case modifications not saved
			if self.check_if_modified():
				if mbox.askokcancel("Warning", "Do you want save changes before moving?"):
					#validate form first, before proceeding to modifying the current patient open on screen and moving to previous patient
					if self.validate_form():
						self.modify()
					else:
						return
			self.index -= 1
			self.set_values()
			
	def check_if_modified(self):
		"""
			We want to check if form was modified , in case user clicks previous or next.
			We compare whether values in textfields differ from lst_of_patients_copy
		"""
		if self.name_entry.get() != self.lst_of_patients_copy[self.index]['name']:
			return True
		elif self.lst_of_patients_copy[self.index]['address'] != self.address_entry.get():
			return True
		elif self.lst_of_patients_copy[self.index]['birthday'] != self.birthday_entry.get():
			return True
			
		return False
		
	#close the add patient dialog . This is close button clicked.
	def close(self):
		self.top.destroy()

	#the save all button click will update initial list and UI with changes. and close the modify screen
	def save_all(self):
		#in case modify, and we modified like 10 patients. Update initial list. Note this will work always on save all button, 
		# in case user closes the dialog with 'X' BUTTON on corner I am assuming
		# he cancelled the modifications he did.
		
		#validate form first, before proceeding to saving the current patient open on screen and closing the box + updating UI.
		if self.validate_form():
			#make sure to modify last patient opened on screen before saving all.
			self.modify()
			self.lst_of_patients = copy.deepcopy(self.lst_of_patients_copy)
			self.function_update(self.lst_of_patients)
			self.top.destroy()