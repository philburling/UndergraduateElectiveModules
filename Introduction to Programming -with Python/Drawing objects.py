# Filename: Drawing objects
# Title: Drawing objects
# Description: Imports functions from a 'drawing' module, and uses them to draw
# a line of 6 $ characters, a square with each side made of 10 asterisks and a
# triangle 5 characters high that is made up of '%' characters.
# Author: Philip Burling
# Date: 11/03/07

import drawing

drawing.line(6,'$')

print ''

drawing.square(10,'*')

print ''

drawing.triangle(5,'%')

print ''

raw_input("<<<Press any key to terminate the program>>>")
