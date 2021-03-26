#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Thu March 25 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


import os

def findFiles(d, myDictionary):
	for path in os.listdir(d):
		full_path = os.path.join(d, path)
		if os.path.isfile(full_path):
			head,tail = os.path.split(full_path)
			if tail != ".DS_Store":
				myDictionary['files'].append(full_path)
				print("Found a file with path" , full_path)
		elif  os.path.isdir(full_path):
			head,tail = os.path.split(full_path)
			if tail.isupper():
				myDictionary['foldersCaptial'].append(full_path)
				print("Found path to a folder that have capital letters in their name",full_path)
			
			findFiles(full_path,myDictionary)
			
			
d = input("Which folder you want to analyze?\n")
myDict = {'files':[] ,"foldersCaptial": []}
if os.path.exists(d): 
	findFiles(d,myDict)
	print("\n------------Files---------------")
	print(myDict['files'])
	print("\n------------Folders---------------")
	print(myDict['foldersCaptial'])