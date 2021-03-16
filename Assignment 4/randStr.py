#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed February 24 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================

from functools import reduce 
import random

def randWord(text, seedValue=None):
	if(seedValue!=None):
		random.seed(seedValue)
	# split text , we will get list of words
	words=text.split()
	# generate random number between 1 & len(words)
	num = random.randint(1,len(words))
	# that random number - 1 , is  our selected random word.
	return words[num-1]

def strMixer(text, seedValue=None):
	if(seedValue!=None):
		random.seed(seedValue)
	words=text.split()
	lst = []
	
	# sample() is an inbuilt function of random module in Python that returns a particular length list of items
	# chosen from the sequence
	# i.e. list, tuple, string or set. Used for random sampling without replacement.

	if(len(words) == 1):
		lst = random.sample(words[0],len(words[0]))
	else:
		lst = random.sample(words, len(words))

	return ' '.join(lst)

def randIntForWord(text, seedValue=None):
	seedValue = 0
	if text != "":
		# text = "abc" will make a list of [97,98,99] using list(map(ord, str(text)))
		# we then sum that list using reduce function to get seedValue.
		lst = list(map(ord, str(text)))
		seedValue= reduce(lambda a,b : a+b,lst)
	
	random.seed(seedValue)
	index=random.randint(0,100000)
	return index

if __name__ == "__main__":
	print("Sorry, but this module can only be imported!")