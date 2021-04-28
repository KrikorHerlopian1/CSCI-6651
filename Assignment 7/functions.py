#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue Apr 27 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================

import datetime
__author__ = "Krikor Herlopian"
__copyright__ = "Copyright 2021, University of New Haven Final Assignment"

"""
	Functions used multiple places. Like center_window is used many places to center the screens ( dialogs, original screen etc)
"""
#center the window, tkinter screen. size specified for screen too.
def center_window(root,width=200, height=150):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

def valid_date(inputDate):
	"""
		Check if date is valid. If its valid return true, else return false
	"""
	isValidDate = True
	try:
		day,month,year = inputDate.split('/')
		datetime.datetime(int(year),int(month),int(day))
	except:
		isValidDate = False
	if(isValidDate) :
		return True
	else :
		return False