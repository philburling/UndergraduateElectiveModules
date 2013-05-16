# Filename: gibbons.py
# Title: Gibbon Racing
# Function:
# Author: Philip Burling
# Date: 16/02/07


n=raw_input('Enter the number of gibbons in the race: ')


# This section ensures that the user has entered a valid number of gibbons. If
# not then the user is told what is wrong with the entry and prompted to enter
# a new one.

while (type(n) != int):
    try:
        n = int(n)
    except:
        try:
            n = float(n)
            print ''
            print 'Error! Only whole gibbons can compete.'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')
        except:
            print ''
            print 'Error! The number entered must be a digit. (e.g. \'3\' but not \'three\')'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')

while (n<3) or (n>6):
    if (n<0):
        print ''
        print 'Error! No such thing as a negative gibbon.'
        print ''
        n=raw_input('Enter the number of gibbons in the race: ')
    elif (n>6):
        print ''
        print 'Error! There cannot have been more than 6 gibbons in the race.'
        print ''
        n=raw_input('Enter the number of gibbons in the race: ')
    elif (n<3) and (n<-1):
        print ''
        print 'Error! There must have been at least three gibbons.'
        print ''
        n=raw_input('Enter the number of gibbons in the race: ')


# In the next section, the user is asked to enter the name and then time of each
# gibbon in turn. For each time entered, if it is a negative time, the user will
# be told that the times entered must be positive and then they will be prompted
# to enter a new time.

# Note: I will allow for a time of 0 seconds as the gibbons time may have been a
# matter of milliseconds (and therefore could have been potentially rounded down
# to zero seconds).

q=1
mintime = -1

print''

while not q>n:
    r = str(q)
    name = raw_input('Enter the name of gibbon no.'+r+': ')
    print ''
    newtime = raw_input('Enter '+name+'\'s time (in seconds): ')
    newtime = int(newtime)
    while newtime<0:
        print ''
        print 'Error! Times must be positive'
        print ''
        newtime = raw_input('Enter '+name+'\'s time (in seconds): ')
    print '' 
    if newtime<mintime or mintime==-1:
        mintime = newtime
        winner = name
    q = q+1

# The next few sections handle the format and presentation of the results that
# will be presented to the user.

# Here all the numerical components to be included as part of the output of the
# solution are represented as variables. The value of each variable is
# determined by its appropriate equation:

hours = mintime/3600
minutes = (mintime%3600)/60
seconds = (mintime%3600)%60


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


# The next section deals with what form the time will be displayed in the output.
# It handles a separate case for when there are no hours to when there are hours.
# If there are hours then an entry for hours will be included in the output,
# else the output will include only entries for minutes and seconds. 

if hours != 0:
    timeoutput = hours, h, minutes, m, seconds, s
else:
    timeoutput = minutes, m, seconds, s


# This next section is the line that presents the winning gibbon and its time to
# the user.


print 'The winning gibbon was', winner, 'with a time of', timeoutput

# These last two lines are simply there so that the user has time to view the
# output before the program terminates. The user now determines when it
# terminates.

print ''
input("<<<Press 'Enter' to terminate the program>>>")
