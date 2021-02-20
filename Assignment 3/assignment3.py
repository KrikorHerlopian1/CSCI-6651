#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Mon February 15 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================

import re
import sys
import getopt

wordsDict = {}
lettersDict = {}

def cleanupLine(line):
    return re.sub(r"[^a-zA-Z0-9']+", " ", line)


def countWords(line):
    global wordsDict
    
    words = line.lower().split()

    for word in words:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1
    return wordsDict


def countLetters(line):
    global lettersDict
    for i in line.lower(): 
    	if i >= '0' and i <= '9' or i == '\'':
    		continue;
    	elif i in lettersDict: 
        	lettersDict[i] += 1
    	else: 
       		lettersDict[i] = 1
    return lettersDict


def readFiles(filename):
    handle = open(filename, 'r')
    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)

def results():
	# read file 1
	readFiles('File1.txt')
	list = []
	listWords = []
	# check if e is in lettersDict, append to list how many times. Else append 0.
	if 'e' in lettersDict:
		list.append(lettersDict['e'])
	else:
		list.append(0)
	
	# check if to is in wordsDict, append to listwords how many times. Else append 0.
	if 'to' in wordsDict:
		listWords.append(wordsDict['to'])
	else:
		listWords.append(0)
		
	# clear the dictionaries to read file 2.
	lettersDict.clear()
	wordsDict.clear()
	
	# read file 2
	readFiles('File2.txt')
	# check if t is in lettersDict, append to list how many times. Else append 0.
	if 't' in lettersDict:
		list.append(lettersDict['t'])
	else:
		list.append(0)
		
	# check if the is in wordsDict, append to listwords how many times. Else append 0.	
	if 'the' in wordsDict:
		listWords.append(wordsDict['the'])
	else:
		listWords.append(0)
	
	# clear the dictionaries to read file 3.
	lettersDict.clear()
	wordsDict.clear()
	
	# read file 3
	readFiles('File3.txt')
	# check if w is in lettersDict, append to list how many times. Else append 0.
	if 'w' in lettersDict:
		list.append(lettersDict['w'])
	else:
		list.append(0)
		
	
	# check if computer is in wordsDict, append to listwords how many times. Else append 0.	
	if 'computer' in wordsDict:
		listWords.append(wordsDict['computer'])
	else:
		listWords.append(0)	
		
	# extend list of words to list of letters.
	list.extend(listWords)
	return list 




def main(argv):    
	opts, args = getopt.getopt(argv, "hf:l:w:") 
	inputfile = []  
	letter = []
	word = []
	
	#read all arguments, add all arguments given with -f to inputfile list. -l add to letters list, -w add to wordlist
	#make sure -l given is a letter.
	for opt, arg in opts:       
		if opt == '-h':            
			print('krikor_h_assignment3.py -f <file1> -f <file2> -l letter1 -l letter2 -w word1 -w word2 ')            
			sys.exit()        
		elif opt == "-f":            
			inputfile.append(arg)            
		elif opt == "-l":                      
			if(len(arg) == 1 and arg.isalpha()):
				letter.append(arg)    
			else:
				print('-l argument should be one letter ,',  arg, "is not a one letter" )
				sys.exit()    
		elif opt == "-w":            
			word.append(arg)                
	
	#if no files given (-f argument), print no inputfile specified.
	if(len(inputfile) == 0):
		print("No Inputfile specified")
		sys.exit()
	
	#loop over all files
	
	for file in inputfile:
		# clear the dictionaries, since its global variable and previous file results are stored in them.
		lettersDict.clear()
		wordsDict.clear()
		print("\n------------",file,"-----------------")
		# if readfile fails, the path or file is wrong. Move to next file in the loop.
		try:
			readFiles(file)
		except FileNotFoundError:
			print("Wrong file or file path")
			continue
		
		fileDict = {}
		#loop over letters, then over words and check their presence in file.	
		for l in letter:
			if l in lettersDict:
				fileDict[l] = lettersDict[l]
			else:
				fileDict[l] = 0
		for w in word:
			if w in wordsDict:
				fileDict[w] = wordsDict[w]
			else:
				fileDict[w] = 0
		print(fileDict)
	
		

# if you call results function, it will read file1.txt file2.txt file3.txt. And will check frequencies of 
# how many times 'e' and 'to' show up in file 1.
# how many times 't' and 'the' show up in file 2.
# how many times 'w' and 'computer' show up in file 2.
print("--------------------------Results Function---------------------------\n")
print(results(),"\n")

# use the command line to pass the file letter and word you want to check for.
print("--------------------------Main Function--------------------------------")
main(sys.argv[1:])

