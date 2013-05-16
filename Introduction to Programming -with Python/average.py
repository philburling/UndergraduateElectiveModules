# Filename: average.py
# Title: Calculate the mean average of five numbers
# Function: This program is for calculating the mean average of 5 numbers from user input
# Author: Philip Burling
# 30/01/2007

# This section gathers the numbers to be processed from the user's input

first = input('Enter the First Number: ')
second = input('Enter the Second Number: ')
third = input('Enter the Third Number: ')
fourth = input('Enter the Fourth Number: ')
fifth = input('Enter the Fifth Number: ')

# This line computes an average from the five numbers the user has entered

print 'The mean average of those numbers is: ',(first+second+third+fourth+fifth)/5.0
