#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Tue April 06 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================



class Person:
	"""class Person with attributes first_name, last_name, and account."""
	count = 0
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.__class__.count += 1
		self.__account = self.__class__.count
		
		
	def print_data(self):
		print("\nfirst name: ",self.first_name,"\nlast name:", self.last_name,"\naccount:", self.__account)
		
	def get_account(self):
		return self.__account
		
		
		
me = Person("Krikor","Herlopian")
friend = Person("Mehdi", "Mekni")

print("\n---------------------------")
print(me.__doc__)
print(friend.__doc__)

print("\n---------------------------")
print(me)
print(friend)

print("\n---------------------------")
me.print_data()

friend.print_data()


print("\n---------------------------")
print(me.get_account())
print(friend.get_account())