#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue Apr 27 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


from tkinter import *
import tkinter.filedialog
from tkinter import messagebox as mbox
import json
import copy

#background color of window, and also listbox. Background color everywhere.
bg_color = '#D9D9D9'


#add/modify a patient dialog
class AddModifyPatientDialog:
	def __init__(self, parent,modify=False):
		global lst_of_patients
		top = self.top = Toplevel(parent)
		#in case user clicks the top right X button to close, call on_closing function
		top.protocol("WM_DELETE_WINDOW", self.on_closing)
		#set background color
		top.configure(background=bg_color)
		#copy of list of patients, when modifying we want to modify the copy up until user clicks close.
		self.lst_of_patients_copy = copy.deepcopy(lst_of_patients)
		#when modifying, modifications starts from index 0. Top of the list.
		self.index = 0
		#center dialog on screen, a little bit more height if modifying ( for previous and next buttons). Also set the title whether modify patient or add patient.
		if modify:
			top.title("Modify Patient")
			self.center_dialog_window(360,150)
		else:
			top.title("Add a Patient")
			self.center_dialog_window(360,120)
		
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
		
		#fit in same row/column two buttons together. In case its modify patient fit on 5th row, in case add patient on 4th row. 
		#if modify also add prev next buttons on 4th row this time
		#note rows start from Zero.
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
		global lst_of_patients
		json  = { "name": self.name_entry.get(), "address": self.address_entry.get(), "birthday": self.birthday_entry.get()}
		lst_of_patients.append(json)
		update_list()
		self.top.destroy()
		
	#in case its modify	, we set the values on screen of patient we are editing.
	def set_values(self):
		global lst_of_patients
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
		
	#close the add patient dialog 
	def close(self):
		#in case modify, and we modified like 10 patients. Update initial list. Note this will work always on close button, in case user closes the dialog with 'X' BUTTON on corner I am assuming
		#he cancelled the modifications he did.
		global lst_of_patients
		lst_of_patients = copy.deepcopy(self.lst_of_patients_copy)
		update_list()
		self.top.destroy()

    #center the window, tkinter screen. size specified for screen too.
	def center_dialog_window(self,width=200, height=150):
		# get screen width and height
		screen_width = self.top.winfo_screenwidth()
		screen_height = self.top.winfo_screenheight()

		# calculate position x and y coordinates
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2)
		self.top.geometry('%dx%d+%d+%d' % (width, height, x, y))
        

#file_name is patients file loaded, to be opened by user using this application
#need to make it scrollable vertically the screen, since we might have 1000 patient.
global file_name,scrollbar
file_name = ''
root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

#center the window, tkinter screen. size specified for screen too.
def center_window(width=200, height=150):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    

#show file dialog to open patients file.
def open_file():
	try:
		global file_name
		#for now you can only open .json files.
		result = tkinter.filedialog.askopenfilename(filetypes=[("Patient File",['.json'])])
		if result:
			file_name = result
			load_file()
	except:
		pass
		
#load the patients from file
def load_file():
	global file_name,lst_of_patients
	with open(file_name, "r") as op:
		lst_of_patients = json.load(op)
		destroy_label()
		#let us add listview to the screen. Since we dont know number of patients, we need to make it
		# scrollable.
		update_list()
		
#let us add listview to the screen. Since we dont know number of patients, we need to make it
# scrollable.	
def update_list():
	global list_box, lst_of_patients,scrollbar
	#destroy the previous list, in case new patients file loaded.
	try:
		if list_box:
			list_box.destroy()
	except:
		pass
	list_box = Listbox(root, yscrollcommand = scrollbar.set , width= 400, bg=bg_color)
	for patient in lst_of_patients:
		list_box.insert(END, patient['name']+","+patient['address']+","+patient['birthday'])
	list_box.pack( side = LEFT, fill = BOTH )
	scrollbar.config( command = list_box.yview )
	

# show message you cant save without opening a patient file first.
# if opened, show a dialog box to add new patient
def add_patient():
	if file_name:
		inputDialog = AddModifyPatientDialog(root)
		root.wait_window(inputDialog.top)
	else:
		mbox.showinfo("Open a patients file first", "Open a patients file first")	

# show message you cant save without opening a patient file first.
# if opened, save the new list to that patients file
def save_patient():
	if file_name:
		# we are saving json format
		with open(file_name, 'w') as outfile:
			json.dump(lst_of_patients, outfile)
		#show message it saved successfully
		mbox.showinfo("Patients Saved", "successful")
	else:	
		#open a patients file first before proceeding.
		mbox.showinfo("Open a patients file first", "Open a patients file first")	

# show message you cant save without opening a patient file first.
# if opened, show a dialog box to modify patient
def modify_patient():
	if file_name:
		inputDialog = AddModifyPatientDialog(root, True)
		root.wait_window(inputDialog.top)
	else:
		mbox.showinfo("Open a patients file first", "Open a patients file first")				

#INITIALLY the message is load patients file, we want to destroy that label and load list of patients
def destroy_label():
	global label_lst
	try:
		for label in label_lst[:]:
			label.destroy()
			label_lst.remove(label)
	except:
		pass #no label

menubar = Menu(root)

#add file menu, with its submenus.
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="New", command=add_patient)
filemenu.add_command(label="Modify", command=modify_patient)
filemenu.add_command(label="Save", command=save_patient)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#add help menu
filemenuTwo = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=filemenuTwo)

root.config(menu=menubar)
center_window(400,300)
#background of the window
root.configure(background=bg_color)

#make it global, when patient file opened we want to remove all labels on screen and show listbox instead.
global label_lst
label_lst = []
label = Label( root, text="Please load patient file", fg='#000000', bg=bg_color)
label_lst.append(label)
label.pack(side=TOP, anchor=NW)
root.title("My Patient Program")

root.mainloop()



