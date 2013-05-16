#Filename: isLetter.py
#Title: isLetter function
#Function: Defines a function 'isLetter'. This function takes a parameter and
#returns the value 'True' if it is an alphabetic letter, and 'False' if it is
#not. The program demonstrates that the function works by prompting the user to
# enter a character. It then uses the function to decide if the user's entry is
# a letter of the alphabet or not. If it is, it will inform the user that the
# entry was a letter of the alphabet. If it isn't, it will tell them that it
# isn't.
# Author: Philip Burling
# Date: 16/02/07


#I have avoided using the 'string' module in the definition of this function so
#as to make this program independent of other modules. The function first
#creates a list of all the letters in the alphabet, both upper and lower cases.
#It then tries to find the user's entry in the list. If it is successful then it
#will return the value 'True' if unsuccessful, 'False'. Note I have used a list
#rather than a string as the 'isalpha' function in python uses. This is so that
#an entry of more than 1 letter, where the letters happen to be in alphabetical
#order or next to the series of capital letters (e.g. a user entry of 'efgh' or
#'zAB'), will not return the value 'True'. Thus only a letter alone will return
#the value 'True', and a word or random string of alphabetical characters won't.

#This section is the defining of the function

def isLetter (parameter):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if str(parameter) in alphabet:
        return True
    else:
        return False

#This section prompts the user to enter a letter. This is to test that the
#function confirms that an entry is a letter of the alphabet.

end = ''

while end != 'end':
    p = raw_input('Please enter some data (either a letter or not): ')
    print ''
    if isLetter(p) == True:
        print 'The function has recognised your entry as a letter of the alphabet.'
    else:
        print 'The function has recognised your entry as not being a letter of the alphabet.'
        print ''
        print 'Either the entry was not a letter or the entry was more than one letter.'
    print ''
    end = raw_input('Type "end" now if you are finished testing the function (other wise enter anything else): ')
    print ''
