#Filename: caesar-cypher.py
#Title: A Rot13 Caesar Cypher
#Function: This program asks the user to enter the name of a text file. If the
#the file can be opened, the program opens the file and translates the text such
#that all of the letters in it are replaced with letters 13 places from where
#they were in the alphabet. If this would translate any letter beyond the end of
#the alphabet, the letter will instead be transformed to the letter the
#remaining number of places in from the start of the alphabet (i.e. the pattern
#wraps). The translated text is then saved over the original text file.
#Author: Philip Burling
#Date: 16/02/07

#Section for defining functions for encoding


#This section defines the function that will be used to determine whether each
#character in the opened file is a letter of the alphabet or not (and therefore
#whether it needs to be altered). I considered importing the 'string.py' module,
#and then using the line 'if str(parameter) in string.ascii_letters:' to match
#the character. However, I wanted the function to be module independent, so I
#created my own list.

def isLetter(parameter):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if str(parameter) in alphabet:
        return True
    else:
        return False

#This section defines the function 'rot13' which translates any letter in the
#file into the letter 13 places away from it in the alphabet (where the letters
#wrap in the alphabet sequence such that 'a' will become 'n' and 'm' will
#become 'b' once translated by the function).
#Rather than identifying each letter and then assigning it a new letter as
#its value (involving a separate 'if' condition for each letter translation),
#the function simply finds the ASCII value for that letter, adds 13 to it
#then finds the corresponding letter to the new value, which is then stored as
#the new letter. So that the translation wraps (i.e. it only involves the
#alphabet ASCII values), for anything within the range of ASCII values
#corresponding to the capital letters 'N' to 'Z', 13 is deducted from the ASCII
#value. This is because, as there are 26 (2x13) letters in the sequence and the
#sequence wraps, a translation forwards should equate to a translation backwards
#in terms of the letters. A translation forwards, in terms of ASCII values would
#possibly equate to a character outside of the alphabetical sequence, which is
#why a translation backwards must be used instead for letters past 'M'.

#Before translation, the function will establish whether an upper-case or lower
#case letter is involved. This information is stored as a string in the 'case'
#variable, which is initially set to 'upper'. However, if the letter is found to
#be lower-case, it will be given the string value 'lower'. This is so that the
#letter translation part of the function only has to deal with one range of
#ASCII values (the range concerning the upper-case). If the value of 'case' is
#'lower' after translation, the function will transform the letter it back to
#a lower-case letter is it was earlier.

def rot13(letter):
    case = 'upper'
    if letter.islower() == True:
        case = 'lower'
        letter = letter.upper()
    n = ord(letter)
    if (n>64 and n<78):
        n = n+13
    elif (n>77 and n<91):
        n = n-13
    letter = chr(n)
    if case == 'lower':
        letter = letter.lower()
    return letter

#Section for opening file

try:
    filename = raw_input('Enter the name of the text file you wish to encode: ')
    readfile = open(filename,'r')
    print ''
except:
    print ''
    print 'Cannot open file to read'
    print ''
    raw_input('<<<Press Return to quit>>>')
        

#Section for storing the information from the file as a string in a variable
#'fulltext', and for creating a new variable 'newtext' to store the data after
#it has been translated. Then it will be ready to be saved on to the file.

fulltext = readfile.read()
newtext = ''

#The file is closed at this point so that it can be re-opened later to write to,
#rather than read from. It is no longer needed to be read, as the information it
#contained is stored in the variable 'fulltext'.

readfile.close()

#This is the section for performing the letter translation. All characters,
#manipulated or not, are appended to the initially empty string in the variable
#'newtext'.

for char in fulltext:
    if isLetter(char) == True:
	    char = rot13(char)
    newtext = newtext+char

#This is the section for writing back to the file. The file is re-opened to be
#written too, and the string information in 'newtext' overwrites what was
#originally there.

writefile = open(filename,'w')

try:
    writefile.write(newtext)
except:
    print 'Error trying to write to file'
    print ''
    raw_input('<<<Press Return to quit>>>')

#Section for closing the file. After this has been done, the file will appear
#changed when reopened in other programs.

writefile.close()



