# File: maths -using "trial and error" method.py
# Title: Mathematical functions and trial and error
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


# This next section first tries to calculate the square root. If it is unable to
# do so, it alerts the user that the number entered must not have been positive
# and so no solution will be printed. If the calculation is successful the
# square root is printed as a solution. The program then tries to calculate the
# cubed root of the number. However, if it had made it past the first
# calculation, it will make it past this one. The cube root is then printed as a
# solution for the user to see. The square and cube roots will never be positive
# as python always gives the positive solution as an answer by default.

try:
    m = math.sqrt (n)
    print "The square root of that number is:", m
    print ""
    q = math.pow (n,(1/3.0))
    print "The cube root of that number is:", q
except:
    print "The number was not positive -therefore no square or cube root will be given"

# These last two lines allow the data to stay on the screen till the user wishes
# to terminate the program.

print ""
raw_input("<<<Press ENTER to exit>>>")
