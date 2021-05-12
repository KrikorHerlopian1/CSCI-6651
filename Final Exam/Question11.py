#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


import re

password_lst = input("Type your password list seperated by comma\n")
password_lst = password_lst.split(",")

# we will append in this list, the correct passwords entered.
correct_passwords = []
for password in password_lst:
    
    #in case password length less than 6 or greater than 12,continue to next password as this one not valid.
    if len(password) < 6 or len(password) > 12:
        continue
	#in case 0-9 not found, continue to next password as this one not valid.
    elif not re.search("([0-9])+", password):
        continue
	#in case a-z not found, continue to next password as this one not valid.
    elif not re.search("([a-z])+", password):
        continue
	#in case A-Z not found, continue to next password as this one not valid.
    elif not re.search("([A-Z])+", password):
        continue
	#in case $#@ not found, continue to next password as this one not valid.
    elif not re.search("([@$#])+", password):
        continue

    else:
        correct_passwords.append(password)

print((" ").join(correct_passwords))