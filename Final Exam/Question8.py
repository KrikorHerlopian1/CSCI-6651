#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


result = 0
while True:
    d_w_value = input()
    #in case enters enter, line empty break with final result in result.
    if d_w_value == "":
        break
    else:
        d_w_value = d_w_value.split(" ")#split by space. first will be either D or W..the second number.
        
        #D add to result, W negate.
        if d_w_value[0] == "D":
            result = result + int(d_w_value[1])
        elif d_w_value[0] == "W":
            result = result - int(d_w_value[1])

print(result)