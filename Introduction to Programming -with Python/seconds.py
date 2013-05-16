# Filename: seconds.py
# Title: Time conversion
# Function: To express an integer entered by the user, which stands for a number
# of seconds, in terms of hours, minutes and seconds.
# Author: Philip Burling
# Date: 14/02/07



n = input('Enter the number of seconds: ')


# The the following section tells the user if they have entered a negative
# number, and if they have, asks them if they still want to convert it.
# If the user replies 'no' then they will be asked to enter a new number.
# If the user replies 'yes', then a variable 'neg' will be set to a value of
# 'yes' so that the program knows that it needs to:
# (a) convert the number of seconds into a positive integer so that the
#     remainder (modulus) function will not round negative numbers down to the 
#     next whole number below (i.e. '-1.3' would be rounded to '-2' which is
#     incorrect as '-1.3' should only stand for 'minus' at least one second)
# (b) alter the output to display negative hours minutes and seconds.



neg = 'no'
while (neg == 'no') and (n<0):
    print ''
    print 'Negative number entered'
    neg = raw_input('Do you still wish to convert this number? (yes/no): ')
    while (neg != 'yes') and (neg != 'no'):
        print ''
        print 'You must answer either "yes" or "no" '
        print ''
        neg = raw_input('Do you still wish to convert this number? (yes/no): ')
    if neg == 'no':
        print ''
        n = input('Enter a new number of seconds: ')

# Here the number entered by the user is made positive if already negative.
# Then all the numerical components to be included as part of the output of the
# solution are represented as variables. The value of each variable is
# determined by its appropriate equation:

if neg == 'yes':
    n = n*-1

hours = n/3600
minutes = (n%3600)/60
seconds = (n%3600)%60


# This section takes care of the grammer in the special cases when there will
# be just one (or a combination of) hour, minute or second in the output.
# It does this by using variables to stand for the words used, the value of
# each is determined by whether the variable for the corresponding unit of time
# is equal to '1' or not. The variable for each word will be expressed as the
# actual word in the output of the solution.

if (hours == 1):
    h = 'hour,'
else:
    h = 'hours,' 

if (minutes == 1):
    m = 'minute,'
else:
    m = 'minutes,'

if (seconds == 1):
    s = 'second'
else:
    s = 'seconds'


# The next section deals with how the solution will appear on the screen to the
# user. The first 'if' condition handles whether the data needs to be negated
# when displayed -an alteration required if the number of seconds entered by the
# user was negative. The second 'if' condition deals with the case of when there
# are no hours. If there are hours then an entry for hours (in either
# positive negative cases) will be included in the output, else the output will
# include only entries for minutes and seconds. 

print ''



if neg == 'yes':
    print n*-1, 'seconds is equivalent to:'
    print ''
    if hours != 0:
        print hours*-1, h, minutes*-1, m, seconds*-1, s
    else:
        print minutes*-1, m, seconds*-1, s
else:
    print n, 'seconds is equivalent to:'
    print ''
    if hours != 0:
        print hours, h, minutes, m, seconds, s
    else:
        print minutes, m, seconds, s



# These last two lines are simply there so that the user has time to view the
# output before the program terminates. The user now determines when it
# terminates.

print ''
input("<<<Press 'Enter' to terminate the program>>>")
