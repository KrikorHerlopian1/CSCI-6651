#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


print("question 1 ")
print("-------------------------")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list")
print(nums)
print("-------------------------")
print("Even numbers")
even_numbers = list(filter(lambda x: x%2 == 0, nums))
print(even_numbers)