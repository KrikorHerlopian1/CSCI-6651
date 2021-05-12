#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


from string import *

lines = []
print("Enter sequence of lines: ")

while True:
	line = input("> ")
	if not line:
		break
	lines.append(line.upper())

print(lines)