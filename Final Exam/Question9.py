#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


sentence = input("Type your sentence \n")
sentence = list(sentence)

#keep counter for letters, and digits.
letters, digits = 0, 0

#loop over every character in sentence. let us check what each one is.
for c in sentence:
	#its a letter update letter by 1, its digit update digit by 1.
    if c.isalpha():
        letters = letters + 1
    if c.isdigit():
        digits = digits + 1
    else:
        pass # its not a letter or digit , just ignore

print("Letters:", letters)
print("Digits:", digits)