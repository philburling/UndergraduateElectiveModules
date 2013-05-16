# Filename: numbersorter.py
# Title: Number Sorter
# Function: Sorts 10 numbers entered by the user into descending numerical order
# starting the highest first and ending with the lowest. It then prints the new
# order in a list for the user to see.
# Author: Philip Burling
# Date: 28/04/07


# First the program creates an empty list to store the numbers.

numbers = []

# The counter (variable 'n'), for which number is being entered, is set to '1'

n = 1

# A loop asks the user to enter a number and then adds it to the list. It then
# adds 1 to the counter. It does this until the counter has reached 10, such
# that it repeats the process 10 times.

while n <=10:
    number = [input('Enter a number: ')]
    numbers = numbers + number
    n = n+1

# This section sorts the numbers in the list into ascending numerical order and
# then reverses it to put it in descending order.

numbers.sort()
numbers.reverse()

# The next line displays the list to the user

print numbers
