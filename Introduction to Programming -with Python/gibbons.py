# Filename: gibbons.py
# Title: Gibbon Racing
# Function: This program prompts the user to enter the number of gibbons in a gibbon race, the names of the gibbons and their respective times. As the data
# is entered, the program finds the gibbon with the shortest time, then displays the name of the winning gibbon and its time (in the form of hours [if
# needed], minutes and seconds) to the user.
# Author: Philip Burling
# Date: 16/02/07


n=raw_input('Enter the number of gibbons in the race: ')

# This section ensures that the user has entered a positive integer for the
# number of gibbons. If not, then the user is told what is wrong with the entry
# and prompted to enter the number again.

while (type(n) != int) or ((n<3) or (n>6)):
    try:
        n = int(n)
        if (n<0):
            print ''
            print 'Error! No such thing as a negative gibbon!'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')
        elif (n>6):
            print ''
            print 'Error! There cannot have been more than 6 gibbons in the race!'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')
        elif (n<3) and (n>-1):
            print ''
            print 'Error! There must have been at least three gibbons!'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')
    except:
        try:
            n = float(n)
            print ''
            print 'Error! Only whole gibbons can compete!'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')
        except:
            print ''
            print 'Error! The number entered must be a digit. (e.g. \'3\' but not \'three\')'
            print ''
            n=raw_input('Enter the number of gibbons in the race: ')





# In the next section, the user is asked to enter the name and then time of each
# gibbon in turn. For each time entered, if it is a negative time, the user will
# be told that the times entered must be positive and then they will be prompted
# to enter a new time.

# This task is performed through the use of a set of commands that repeat until
# all the data required has been gathered while keeping the relevant data stored
# as values in appropriate variables.
# The program will only keep track of at most two times at once:- that which has
# been the smallest entry so far ('mintime'), and the most recently entered one
# to which that smallest entry is to be compared ('newtime'). If the 'newtime'
# is smaller than the 'mintime', then the 'newtime' is taken as the new
# 'mintime', and the name entered just before it is taken as that of the
# 'winner'
# The first name entered and the first time entered will be stored as the
# initial 'winner' and 'mintime' respectively. The 'winner' and 'mintime' will
# be updated as necessary through each cycle of the loop, until there have been
# as many cycles as the number of gibbons entered earlier. This is kept track of
# by the variable 'q' which acts as a counter, starting at 1 and increasing by 1
# for each cycle until it exceeds 'n' (the number of gibbons entered by the
# user).
# The starting value for the winners time ('mintime') is given the arbitrary
# negative value of -1 so that its value can be used as a condition for the
# assignment of the first time entry (first 'newtime') as the initial winning
# time ('mintime').

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

# The program has now separated out the information relevant to the solution
# into two variables: 'mintime' (the shortest time) and 'winner' (the name of
# the gibbon that won with that time).

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
