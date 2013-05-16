# File: maths -using conditionals.py
# Title: Mathematical functions and conditionals
# Function: Prompts the user to enter a number. It then calculates and prints
# the square of that number, and if the number was positive, the square root
# and cube root of that number. It only displays the positive roots.
# Author: Philip Burling
# Date: 04/03/07


# This first line imports the functions from the math module. They are necessary
# for calculating squares, square roots and cube roots.

import math

# User prompted input line

n = raw_input("Enter a number: ")

#This section checks that the data entered by the user is actually a number. If
# not, the user is asked to enter a number again.

while not (type(n) == float):
    try:
        n = float(n)

    except:
        print ""
        print "Error! What you entered was not a number!"
        print ""
        n = raw_input("Enter a number: ")

print ""
print "The square of that number is:", math.pow (n,2.0)
print ""


# This next section tests to see if the number entered was positive. If it was
# then it will calculate and print the positive square root of the number and
# the positive cube root of the number. The roots calculated are checked for
# their positivity, and if they are not positive, they are multiplied by -1 to
# make them positive before printing them. From my own experience python only
# gives the positive values of roots anyway, but this extra measure is there
# just in case there are exceptions for data I haven't tried.

if n >= 0:
    m = math.sqrt (n)
    if m < 0:
        m = m*-1
    print "The square root of that number is:", m
    q = math.pow (n,(1/3.0))
    if q < 0:
        q = q*-1
    print ""
    print "The cube root of that number is:", q

# These last two lines allow the data to stay on the screen till the user wishes
# to terminate the program.

print ""
raw_input("<<<Press ENTER to exit>>>")
