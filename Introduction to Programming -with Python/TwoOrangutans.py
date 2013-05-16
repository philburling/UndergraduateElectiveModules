# Filename: TwoOrangutans.py
# Title: Two Orangutans
# Function: Creates two Orangutan objects from user given names and initial
# co-ordinates. The program then displays how far (in a straight line) the two
# Orangutans are from each other.
# Author: Philip Burling
# Date: 28/04/07


# This line imports the class 'OrangUtan' from the file 'OrangUtan.py' along
# with all of the functions that may be used with it.

from OrangUtan import *

# The next section gathers the data for the first Orangutan from user-input.
# This involves creating two empty variables for the 'x' and 'y' co-ordinates
# so that loops can be created to facilitate the user, should they enter the
# wrong kind of data for either of the co-ordinates.

name1 = raw_input('Enter the name of the first Orangutan: ')

x1 = ''
y1 = ''

print ''

while x1 == '':
    try:
        x1 = input('Enter the x co-ordinate of the first Orangutan: ')
        print ''
    except:
        print ''
        print 'Error!. Entry must consist solely of digits.'
        print ''

while y1 == '':
    try:
        y1 = input('Enter the y co-ordinate of the first Orangutan: ')
        print ''
    except:
        print ''
        print 'Error!. Entry must consist solely of digits.'
        print ''

# This next section gathers the data for the second Orangutan in exactly the
# same way as for the first (see above for explanation of the code).

name2 = raw_input('Enter the name of the second Orangutan: ')

x2 = ''
y2 = ''

print ''

while x2 == '':
    try:
        x2 = input('Enter the x co-ordinate of the second Orangutan: ')
        print ''
    except:
        print ''
        print 'Error!. Entry must consist solely of digits.'
        print ''

while y2 == '':
    try:
        y2 = input('Enter the y co-ordinate of the second Orangutan: ')
        print ''
    except:
        print ''
        print 'Error!. Entry must consist solely of digits.'
        print ''

# The following section constructs the two 'OrangUtan' objects ('O1' and 'O2')
# from the collected data.

O1 = OrangUtan(name1,x1,y1)
O2 = OrangUtan(name2,x2,y2)

# The next section uses a function associated with the 'OrangUtan' class to find
# the distance between two 'OrangUtan' objects 'O1' and 'O2'.

print name1, 'is', O1.distanceFrom(O2.getX(),O2.getY()), 'units from', name2
print ''
raw_input('<<< Press Enter to exit >>>')
