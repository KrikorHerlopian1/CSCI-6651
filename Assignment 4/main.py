#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Krikor Herlopian
# Created Date: Wed February 24 2021
# Email Address: kherl1@unh.newhaven.edu
# =============================================================================


import randStr

s1 = "Hello, this is my test string and should only be one word in return"
t1 = randStr.randWord(s1, "a")
t3 = randStr.randWord(s1, "b")
t4 = randStr.randWord(s1, 5)
t5 = randStr.randWord(s1)
t6 = randStr.randWord(s1)
t2 = randStr.randWord(s1, "a")

print("""s1 = "Hello, this is my test string and should only be one word in return""")
print("""t1  = randStr.randWord(s1, "a") = """, t1)    
print("""t2 = randStr.randWord(s1, "a") = """, t2)  
print("""t3 = randStr.randWord(s1, "b") = """, t3)  
print("""t4 = randStr.randWord(s1, 5) = """, t4)  
print("""t5 = randStr.randWord(s1) = """, t5)  
print("""t6 = randStr.randWord(s1) = """, t6)    

print("")

s1 = "FRANK"
t1 = randStr.strMixer(s1)
t2 = randStr.strMixer(s1)
t3 = randStr.strMixer(s1)
t4 = randStr.strMixer(s1)

print("""s1 = "FRANK" """)
print("t1 = randStr.strMixer(s1) = ",t1)
print("t2 = randStr.strMixer(s1) = ",t2)
print("t3 = randStr.strMixer(s1) = ",t3)
print("t4 = randStr.strMixer(s1) = ",t4)

t1 = randStr.strMixer(s1,9)
t2 = randStr.strMixer(s1,9)
t3 = randStr.strMixer(s1,9)
t4 = randStr.strMixer(s1,9)


print("t1 = randStr.strMixer(s1,9) = ",t1)
print("t2 = randStr.strMixer(s1,9) = ",t2)
print("t3 = randStr.strMixer(s1,9) = ",t3)
print("t4 = randStr.strMixer(s1,9) = ",t4)


print("")

s1 = "Hello, this is my test string and should only be one word in return"
t1 = randStr.strMixer(s1)
t2 = randStr.strMixer(s1)
t3 = randStr.strMixer(s1)
t4 = randStr.strMixer(s1)

print("s1 = Hello, this is my test string and should only be one word in return ")
print("t1 = randStr.strMixer(s1) = ",t1)
print("t2 = randStr.strMixer(s1) = ",t2)
print("t3 = randStr.strMixer(s1) = ",t3)
print("t4 = randStr.strMixer(s1) = ",t4)

t1 = randStr.strMixer(s1,9)
t2 = randStr.strMixer(s1,9)
t3 = randStr.strMixer(s1,9)
t4 = randStr.strMixer(s1,9)
print("t1 = randStr.strMixer(s1,9) = ",t1)
print("t2 = randStr.strMixer(s1,9) = ",t2)
print("t3 = randStr.strMixer(s1,9) = ",t3)
print("t4 = randStr.strMixer(s1,9) = ",t4)

print("")

n1_0 = randStr.randIntForWord("hello")
n2_0 = randStr.randIntForWord("")
n3_0 = randStr.randIntForWord(55)
n1_1 = randStr.randIntForWord("hello")
print("""n1_0 = randStr.randIntForWord("hello") = """, n1_0)
print("""n2_0 = randStr.randIntForWord("") = """, n2_0)
print("""n3_0 = randStr.randIntForWord(55) = """, n3_0)
print("""n1_1 = randStr.randIntForWord("hello") = """, n1_1)

n1 = randStr.randIntForWord("hello", "s")
n2 = randStr.randIntForWord("hello", "s")
print("""n1 = randStr.randIntForWord("hello", "s") = """, n1)
print("""n2 = randStr.randIntForWord("hello", "s") = """, n2)



n1 = randStr.randIntForWord("hello", "s")
n2 = randStr.randIntForWord("hello", "t")
n3 = randStr.randIntForWord("hello", "x")
print("""n1 = randStr.randIntForWord("hello", "s") = """, n1)
print("""n2 = randStr.randIntForWord("hello", "t") = """, n2)
print("""n3 = randStr.randIntForWord("hello", "x") = """, n3)



