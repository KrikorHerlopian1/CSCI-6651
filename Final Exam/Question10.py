#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


d=dict()
s=input("Enter the string:\n")

#loop over the string
for i in s.split():
	#say first string New, d['New] = d.get('New',0)+1. That means d['New'] = 0+1 = 1
	#next time we get another New it will be d['New] = d.get('New',0)+1. That means d['New'] = 1+1 = 2
	d[i]=d.get(i,0)+1

#sort and prints keys/values
for key,value in sorted(d.items()):
	print(key,":",value)