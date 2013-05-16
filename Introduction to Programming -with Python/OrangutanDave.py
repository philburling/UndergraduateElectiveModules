# Filename: OrangutanDave.py
# Title: Dave the Orangutan
# Function: Creates an object (an orangutan called Dave) and gives it the
# co-ordinates (2,2). The program then displays how far (in a straight line)
# 'Dave' is from the point (5,3) where his favourite food is.
# Author: Philip Burling
# Date: 28/04/07

# This line imports the class 'OrangUtan' from the file 'OrangUtan.py' (which
# should be in the same directory) along with its associated functions.

from OrangUtan import *

# This line creates the object 'Dave' of the class 'OrangUtan' and assigns it a
# name, x co-ordinate and y co-ordinate.

Dave = OrangUtan('Dave',2,2)

# This line prints the distance (as the crow flies) that Dave is from the
# location of the food at (5,3). It finds this distance by calling the function
# 'distanceFrom' from the imported rules from the file 'OrangUtan.py'

print 'Dave is', Dave.distanceFrom(5,3), 'units from his food'
