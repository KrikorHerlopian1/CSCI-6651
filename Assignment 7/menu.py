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
import functions as func
import patient as patient
__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"



class MainMenu(Menu):
	def __init__(self,root,parent,scrollbar,bg_color,label_lst):
		Menu.__init__(self,parent)
		self.root = root
		self.lst_of_patients = []
		self.file_name = ''
		self.scrollbar = scrollbar
		self.bg_color = bg_color
		self.label_lst = label_lst
		#add file menu, with its submenus(Open, New, Modify, Save, Exit).
		filemenu = Menu(self, tearoff=0)
		filemenu.add_command(label="Open", command=self.open_file)
		filemenu.add_command(label="New", command=self.add_patient)
		filemenu.add_command(label="Modify", command=self.modify_patient)
		filemenu.add_command(label="Save", command=self.save_patient)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=parent.quit)
		self.add_cascade(label="File", menu=filemenu)
		
		#add help menu
		filemenuTwo = Menu(self, tearoff=0)
		self.add_cascade(label="Help", menu=filemenuTwo)

	def open_file(self):
		try:
			#for now you can only open .json files.
			result = tkinter.filedialog.askopenfilename(filetypes=[("Patient File",['.json'])])
			if result:
				self.file_name = result
				self.load_file()
		except:
			pass
		
	#load the patients from file
	def load_file(self):
		with open(self.file_name, "r") as op:
			self.lst_of_patients = json.load(op)
			self.destroy_label()
			#let us add listview to the screen. Since we dont know number of patients, we need to make it
			# scrollable.
			self.update_list()
		
	#let us add listview to the screen. Since we dont know number of patients, we need to make it
	# scrollable vertically. We might have 1 million patients. 	
	def update_list(self,patients_lst=None):
		#destroy the previous list, in case new patients file loaded.
		if patients_lst:
			self.lst_of_patients = patients_lst
		try:
			if self.list_box:
				self.list_box.destroy()
		except:
			pass
		self.list_box = Listbox(self.root, yscrollcommand = self.scrollbar.set , width= 400, bg=self.bg_color)
		#loop over list of patients, and insert them to listbox
		for patient in self.lst_of_patients:
			self.list_box.insert(END, patient['name']+","+patient['address']+","+patient['birthday'])
		self.list_box.pack( side = LEFT, fill = BOTH )
		self.scrollbar.config( command = self.list_box.yview )
	

	# show message you cant save without opening a patient file first.
	# if opened, show a dialog box to add new patient
	def add_patient(self):
		if self.file_name:
			#we pass update_list function as parameter
			inputDialog = patient.AddModifyPatientDialog(self.root,self.lst_of_patients, self.update_list)
			self.root.wait_window(inputDialog.top)
		else:
			mbox.showinfo("Open a patients file first", "Open a patients file first")	

	# show message you cant save without opening a patient file first.
	# if opened, save the new list to that patients file
	def save_patient(self):
		if self.file_name:
			# we are saving json format
			with open(self.file_name, 'w') as outfile:
				json.dump(self.lst_of_patients, outfile)
				#show message it saved successfully
				mbox.showinfo("Patients Saved", "successful")
		else:	
			#open a patients file first before proceeding.
			mbox.showinfo("Open a patients file first", "Open a patients file first")	

	# show message you cant save without opening a patient file first.
	# if opened, show a dialog box to modify patient
	def modify_patient(self):
		if self.file_name:
			#we pass update_list function as parameter
			inputDialog = patient.AddModifyPatientDialog(self.root, self.lst_of_patients,self.update_list,True)
			self.root.wait_window(inputDialog.top)
		else:
			mbox.showinfo("Open a patients file first", "Open a patients file first")				

	#INITIALLY the message is load patients file, we want to destroy that label and load list of patients
	def destroy_label(self):
		try:
			#destroy all labels, remove labels from screen.Especially the "Please load patient file" label 
			for label in self.label_lst[:]:
				label.destroy()
				self.label_lst.remove(label)
		except:
			pass #no label



