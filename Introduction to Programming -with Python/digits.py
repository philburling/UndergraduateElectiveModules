# File: digits.py
# Title: String digit analysis
# Function: Prompts the user to enter a string of digits. Analyses user input
# for the number of instances of each digit and whether any (and how many)
# characters entered are not digits
# Author: Philip Burling
# Date: 06/02/07


entry = raw_input("Enter a string of digits: ")
print "Analysis of:", entry


# This next section assigns a value of zero to 11 different variables.
# The value of each variable henceforth will function as a working total for
# the number of instances of its corresponding digit is found in the string
# entered by the user.
# The first variable 'a' will be for the number of 0s, the 2nd 'b' for 1s and so on
# all the way up to 9. The final variable 'x' is for characters in the string
# that are not digits.

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
x = 0

# The next section scans each character in turn and sequentially checks whether
# it matches any of the the digits 0 to 9. For each match found, '1' is
# added to the value of the variable that corresponds to that number. If the
# character has matches none of these digits, then '1' is added to the value
# of the variable 'x'.

for char in entry:
    if char == "0":
        a = a+1
    elif char == "1":
        b = b+1
    elif char == "2":
        c = c+1
    elif char == "3":
        d = d+1
    elif char == "4":
        e = e+1
    elif char == "5":
        f = f+1
    elif char == "6":
        g = g+1
    elif char == "7":
        h = h+1
    elif char == "8":
        i = i+1
    elif char == "9":
        j = j+1
    else:
        x = x+1

# The next section prints the value of the variables as a list of instances of
# the numbers they stand for. Thus the user is presented with an analysis of the
# string.

print "0s:",a
print "1s:",b
print "2s:",c
print "3s:",d
print "4s:",e
print "5s:",f
print "6s:",g
print "7s:",h
print "8s:",i
print "9s:",j

print ""

# This final section tells the user whether there were any characters in the
# string that were not digits or, alternatively, whether all the characters
# were digits. The program decides which message to print based on whether the
# value of the variable 'x' (which stands for the number of non-digit characters
# in the string) is above zero.

if x>0:
    print x, "characters were not digits."
else:
    print "All characters were digits."
