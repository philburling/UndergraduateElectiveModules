# Filename: drawing 
# Title: Drawing Module
# Description: A set of functions that each use two values to print an object of
# a user entered size and built from a user entered character.
# Author: Philip Burling
# Date: 11/03/07

def line(num,ch):
	ch = str(ch)
	print num*ch

def square(num,ch):
	n = num
	ch = str(ch)
	while n >0:
		print num*ch
		n = n-1

def triangle(num,ch):
	ch = str(ch)
	n = 1
	while n <= num:
		print n*ch
		n=n+1


