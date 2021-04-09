#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Sat April 10 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


class myNumberList:
    def __init__(self, number= None):
        self.lst = []
        if number:
            self.add(number)
    
    def add(self, number):
        if type(number) == int or type(number) == float:
            self.lst.append(number)
        else:
        	print("Only numbers can be added")
    
    def remove(self, number):
        while number in self.lst:
            self.lst.remove(number)
    
    def head(self):
        if len(self.lst) == 0:
            return None
        return self.lst[0]

    def getList(self):
        return self.lst

    def __str__(self):
        return str(self.lst)
    
class myRevOrderedNumberList(myNumberList):
    def __init__(self, number=None):
        super().__init__(number)
    
    def head(self):
        if len(self.lst) == 0:
            return None   
        return self.getList()[0]    
        #return max(self.lst)
    
    def getList(self):
        lstReversed = self.lst[:]
        lstReversed.sort(reverse=True)
        return lstReversed

    def __str__(self):
        lstReversed = self.lst[:]
        lstReversed.sort(reverse=True)
        return str(lstReversed)
    
lst1 = myNumberList(24)
lst1.add("Krikor")
lst1.add(23)
lst1.add(22)
lst1.add(25)
lst1.add(25)
print("lst1 = ",lst1)
print("lst1 head = ",lst1.head())
lst1.remove(25)
lst1.add(50)
print("lst1 = " , lst1)

print("------------------------------------")

lst2 = myRevOrderedNumberList(80)
lst2.add("mehdi mekni")
lst2.add(85)
lst2.add(75)
lst2.add(95)
lst2.add(90)
print("lst2 head = ",lst2.head())
print("lst2 = ",lst2)
