#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed May 12 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================

class CustomException(Exception):#inheritance from Exception class
    """Custom Exception class

    Attributes:
        msg -- an explanation of the error
    """

    def __init__(self, msg):
        self.msg = msg


number = input()

try:
	if not number.strip().isdigit():
		raise CustomException("Error as you didnt enter a number")
	if int(number) < 5:
		raise CustomException("Error as you entered number less than 5")
	elif int(number) > 5:
		raise CustomException("Error as you entered number greater than 5")
except CustomException as custom_exception:
    print(custom_exception.msg)