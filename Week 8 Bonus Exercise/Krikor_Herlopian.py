#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Mon March 15 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================
import re

def search(txt):
	lines = []
	try:
		fil_name = 'POEM-1.TXT'
		with open(fil_name,'r') as op_file:
			lines = op_file.readlines()
	except IOError:
		print("Can't Open ", fil_name)
	i = 0
	change_to_upper = txt
	
	# this will return line number, plust the line if the text we search for is in sentence
	#for i,line in enumerate(lines,i) if txt in line
	


	# one way of doing	
	lst = [ (i, re.sub(change_to_upper, change_to_upper.upper(), line))  for i,line in enumerate(lines,i) if txt in line.split()  ]
	#for a,b in lst:
	#	print(a , b)
		
	# another way just automatically print.
	[print(i, '-', re.sub(change_to_upper, change_to_upper.upper(), line) ,end ='') for i,line in enumerate(lines,i) if txt in line.split() ]
	
	return lst
		
while True:
	txt = input("\nEnter string you want to search(search is case sensitive Hard != hard), press enter without entering anything to escape\n")
	if txt == "":
		break
	else:
		search(txt)	