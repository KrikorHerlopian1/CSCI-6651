#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Thu February 11 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


values = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def num_to_base(num, base):
	#if num is zero, return "0"
	if num == 0:
		return values[0]
	elif num < 0:
		op = -1
	else:
		op = 1

	# make num positive. If its negative multiply by -1.
	num = num*op
	res = ""

	# for ex. base 2  num 5
	# first iteration 5%2 = 1  thus values[1] = 1 , num becomes 2 ( 5 divided by 2).
	# second iteration 2%2 = 0 thus values[0] = 0, num becomes 1 (2 divided by 2)
	# third iteration , 1%2 = 1 thus values[1] = 1 , num becomes 0 (1 divided by 2)
	# 3rd iteration result + 2nd iteration result + 1st iteration result = 101
	while num != 0:
		ind = int(num % base)
		res = values[ind] + res
		num = int(num / base)
		
	# if num was originally negative, add - infront of final result.
	# num 5 would stay 101, num -5 would become -101. 
	if op < 0:
		res = "-" + res
		
	return res
    
def generic_converter(*args):
	list = []
	base = -1
	for x in args:
		#if base is equal to -1, we are reading first argument i.e the base.
		if base == -1:
			#if first argument(x) is not a number , notify user of wrong base.
			if type(x) != int:
				return ['Wrong base']
			#if x is not between 2 & 16, notify user of wrong base.
			elif x < 2 or x > 16:
				return ['Wrong base']
			else:
				#x is a number between 2 & 16, assign it to base and append to list. Move to next iteration.
				base = x
				list.append("base = "+str(x))
		else:
			# reading arguments after base, if the argument is not a number append NA to list.
			# Else  convert the number based on base, and append it to list.
			if type(x) != int:
				list.append("NA")
			else:
				list.append(num_to_base(x,base))
	return list
	
	
print(generic_converter(2,5,10,3))
print(generic_converter(8,5,10))
print(generic_converter(17,5,10))
print(generic_converter(16,15,40,3.5))