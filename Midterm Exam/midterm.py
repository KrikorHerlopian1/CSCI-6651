#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed March 03 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================
import time 

print("\n-----------------Question 1--------------------\n")

MyString = "abcdef"

a = MyString[0]
b = MyString[1]
c = MyString[2]
d = MyString[3]
e = MyString[4]
f = MyString[5]

print("My String content is {0} , {1} , {2} , {3} ,{4} ,{5}".format(a,b,c,d,e,f))
print("MyString indexed from left to right is: {0}:0, {1}:1 , {2}:2 , {3}:3 ,{4}:4 ,{5}:5".format(a, b, c, d, e, f))
print("MyString indexed from right to left is: {0}:-6, {1}:-5 , {2}:-4 , {3}:-3 ,{4}:-2 ,{5}:-1".format(MyString[-6],MyString[-5],MyString[-4],MyString[-3],MyString[-2],MyString[-1]))
print("Character abc extraction", MyString[0:3])
print("Character def extraction", MyString[-3:])

#ace = MyString[0:1] + MyString[2:3] + MyString[-2:-1]
ace  = ""
for x in range(0, len(MyString),2):
	ace = ace + MyString[x:x+1]
print("Character ace extraction", ace)

fedcba= ""
for x in range(len(MyString)-1, -1,-1):
	fedcba += MyString[x]
print("Character fedcba extraction " , fedcba)

print("Character abcd ", MyString[0:4])



print("\n-----------------Question 2 part 1--------------------\n")

listOfFiles = ['poem.txt','poem2.txt']
for arg in listOfFiles:
	fil_name = arg
	try:
		with open(fil_name,'r') as op_file:
			cts = op_file.readlines()
			print('\n',fil_name,'has',len(cts),'lines')
			for ln in cts:
				ln = ln.strip()
				print(ln)
	except IOError:
		print("Can't Open ", fil_name)
		
print("\n-----------------Question 2 part 2--------------------\n")


def readNextLine():
	listOfFiles = ['poem.txt','poem2.txt']
	for arg in listOfFiles:
		fil_name = arg
		count = 0
		print("------------{0}-------------".format(arg))
		try:
			with open(fil_name,'r') as op_file:
				lines = op_file.readlines()
				for line in lines:
					try:
						text = input("Please press enter to read next line:")
						if text == "":
							count += 1
							print("Line{}: {}".format(count, line.strip()))
						else:
							print("you typed some text before pressing enter")
							break
					except ValueError:
						print("Invalid entry please only enter")
		except IOError:
			print("Can't Open ", fil_name)


readNextLine()	


print("\n-----------------Question 2 part 3--------------------\n")


def readNextLine():
	listOfFiles = ['poem.txt','poem2.txt']
	for arg in listOfFiles:
		fil_name = arg
		print("------------{0}-------------".format(arg))
		try:
			with open(fil_name,'r') as op_file:
				lines = op_file.readlines()
				for line in lines:
					print("")
					for m in line.strip():
						print(m, end='', flush=True)
						time.sleep(.25)
		except IOError:
			print("Can't Open ", fil_name)


readNextLine()		
		
		
print("\n-----------------Question 2 part 4--------------------\n")

	
def readNextLine2():
	listOfFiles = ['poem.txt','poem2.txt']
	count = 0
	count1 = 0
	fil_name = listOfFiles[0]
	fil_name1 = listOfFiles[1]
	try:
		with open(fil_name,'r') as op_file:
			with open(fil_name1,'r') as op_file1:
				lines = op_file.readlines()
				lines2 = op_file1.readlines()
				while True:
					try:
						text = input("Please press number to read next line:")
						if text == "1":
							count += 1
							if count < len(lines):
								print("Poem1.txt: Line{}: {}".format(count, lines[count]))
							else:
								print("Poem1.txt: No more lines left to print")
						elif text == "2":
							count1 += 1
							if count1 < len(lines2):
								print("Poem2.txt: Line{}: {}".format(count1, lines2[count1]))
							else:
								print("Poem2.txt: No more lines left to print")
						else:
							print("you typed some  different text before pressing enter")
							break
					except ValueError:						
						print("Invalid entry please  enter 1 or 2")
						break
	except IOError:
		print("Can't Open ", fil_name)


readNextLine2()	


print("\n-----------------Question 2 part 5--------------------\n")

data = "" 

with open('Poem2.txt') as fp: 
    data = "\n" + fp.read() 
  

data += "\n"
  
with open ('Poem2.txt', 'a') as fp: 
    fp.write(data) 
    

with open('Poem2.txt','r') as op_file:
	print(op_file.read())
	
	
	
print("\n-----------------Question 3 part 1--------------------\n")

print("print the numbers: {0},{1},{2}".format(1,2,3))

print("\n-----------------Question 3 part 2--------------------\n")

print("Scores were as following: Ally = {Ally}, John = {John},Ann = {Ann}".format(John=75, Ann=80 , Ally=60))


print("\n-----------------Question 3 part 3--------------------\n")

tu = ( 2, 123.4567, 10000, 12345.67)

print("'file_{:03}: {:.2f} {:.2e} {:.2e}".format(*tu))