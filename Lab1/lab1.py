#!/usr/bin/env python3
#Author: Tirth Jayswal
#Seneca Id= tcjayswal (153799200)
#Date Created = 2022/10/17

try:
	age=int(input('Please enter your age: '))
	print('Your age is ' + str(age))

except TypeError:
	print("Please enter an int value")

def helloWorld():
	print(‘Hello World’)

helloWorld()

