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
import os
import functions as func
import patient as patient

__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"

#menu class . File ( Open, New, Modify, Save, Exit). Help.
#All clicks handled here

class MainMenu(Menu):
	def __init__(self,root,parent,scrollbar,bg_color,label_lst):
		"""
			We put all the file menu here and its submenus (open, new modify save, exit)
		"""
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

	#Open  clicked, let user choose a json patient file to load.
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
			#destroy all labels on screen, so that we set the listbox.
			self.destroy_label()
			# == 0 means file is empty
			if os.stat(self.file_name).st_size == 0:
				self.lst_of_patients = []
			else:
				self.lst_of_patients = json.load(op)	
				#let us add listview to the screen. Since we dont know number of patients, we need to make it
				# scrollable.
				self.update_list()
			#showing message that file is loaded successfully, just in case the file is empty and no more labels on screen. User can know he can add patients
			mbox.showinfo("Success", "File Loaded Successfully.Proceed to adding and modifying")	
	

	#let us add listview to the screen. Since we dont know number of patients, we need to make it
	# scrollable vertically. We might have 1 million patients. 	
	def update_list(self,patients_lst=None):
		#this case will happen, when patients_lst is passed from patient.py file. When user clicked save all , or save on add.
		#we are passing update_list method later on as parameter to AddModifyPatientDialog
		if patients_lst:
			self.lst_of_patients = patients_lst
			
		#destroy the previous list_box, in case new patients file loaded or updating.
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
			#we pass update_list function as parameter.So that on new patient added, i update list_box here.
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
	# or in case a patient file is opened but no patients  in it, inform user that there needs to be patient added on list already in order to modify
	# if opened and patients exist, show a dialog box to modify patient
	def modify_patient(self):
		if self.file_name and len(self.lst_of_patients) > 0:
			#we pass update_list function as parameter
			inputDialog = patient.AddModifyPatientDialog(self.root, self.lst_of_patients,self.update_list,True)
			self.root.wait_window(inputDialog.top)
		else:
			mbox.showinfo("ERROR", "Open a patients file first or add patients if file opened")					

	#INITIALLY the message is load patients file, we want to destroy that label and load list of patients in list_box
	def destroy_label(self):
		try:
			#destroy all labels, remove labels from screen.Especially the "Please load patient file" label 
			for label in self.label_lst[:]:
				label.destroy()
				self.label_lst.remove(label)
		except:
			pass #no label



