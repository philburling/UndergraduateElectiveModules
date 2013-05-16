# Filename: eggs.py
# Title: Eggs and boxes
# Function: To divide a number of eggs (entered by the user) by 6 and subsequently print how many boxes (that can contain 6 eggs) can be filled by them -as well as how many eggs will be left over
# Author: Philip Burling
# 31/01/2007


N = input('Enter the number of eggs: ')
print N,'eggs will fill', N/6, 'boxes (of 6) with', N%6, 'eggs left over.'
