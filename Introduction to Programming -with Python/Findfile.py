# Filename: Findfile.py
# Title: Find a File
# Function: Prompts the user to enter a filename, then displays whether or not a
# file with that name exists in the current directory.
# Author: Philip Burling
# Date: 28/04/07


try:
    filename = raw_input('Enter the name of the file: ')
    readfile = open(filename,'r')
    print ''
    print 'A file with that name EXISTS in the current directory'
    print ''
    raw_input('<<<Press Return to quit>>>')
except:
    print ''
    print 'A file with that name DOES NOT exist in the current directory'
    print ''
    raw_input('<<<Press Return to quit>>>')
