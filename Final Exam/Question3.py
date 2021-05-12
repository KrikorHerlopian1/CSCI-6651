#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


tup = (1,2,3,4,5,6,7,8,9,10)
list1,list2 = [],[]

for i in range(0,5):
    list1.append(tup[i])

for i in range(5,10):
    list2.append(tup[i])

print(list1)
print(list2)