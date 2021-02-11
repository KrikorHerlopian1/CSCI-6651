#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Sat January 30 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


def getSubstringsInList(iterable):
    myList = []
    
    # we use n to know how much to slice. In first iteration we want to slice by one.
    # that is iterable[0:1], iterable[1:2] etc
    # In second iteration we increment n by 1, and we want to start slicing by 2
    # that is iterable[0:2], iterable[1:3] etc
    n = 1
    while n <= len(iterable):
    	# we use m as the index to start slicing from until m+n( aka where to.)
    	# len(iterable) - n to make sure of the index ranges not fall out.
    	m = 0
    	while m <= len(iterable) - n:
    		myList.append(iterable[m:m+n])
    		m += 1
    	n += 1	
    return myList


def getSubstringsWithNoDubs(iterable):
    #now you should remove duplicate strings
    # first call the function to get all substrings 
	myList = getSubstringsInList(iterable)
	res = [] 
	# loop over the list returned (myList), and append it to res if and only if its not added to res already
	for x in myList:
		if x not in res:
			res.append(x)
	return res


s = "ABAC"
list = getSubstringsInList(s)
listNoDubs = getSubstringsWithNoDubs(s)


print(list)
print(listNoDubs)
