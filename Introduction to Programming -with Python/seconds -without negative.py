# Filename: seconds.py
# Title: Time conversion
# Function: To express an integer entered by the user, which stands for a number
# of seconds, in terms of hours, minutes and seconds.
# Author: Philip Burling
# Date: 14/02/07


n = input('Enter the number of seconds: ')


# The following section prompts the user to enter a different number if the
# that they entered previously was negative. It will continue to do this if the
# user continues to enter negative numbers.


while (n<0):
    print ''
    print 'Error! Positive numbers only please'
    print ''
    n = input('Enter a number of seconds: ')

# Here all the numerical components to be included as part of the output of the
# solution are represented as variables. The value of each variable is
# determined by its appropriate equation:

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


# The next section deals with the case of when there are no hours. If there are
# hours then an entry for hours will be included in the output, else the output
# will include only entries for minutes and seconds.

print ''


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

