#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


input_value = input("Enter x,y: \n")
dimens = []
for a in  input_value.split(','):
	dimens.append(int(a))

row_num=dimens[0]
col_num=dimens[1]
two_dimensional_array = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        two_dimensional_array[row][col]= row*col
        
print(two_dimensional_array)