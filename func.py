#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Call to the libraries
import re   # Regular Expression

att     = []  # Metadata of attributes
data    = []  # Data of archive
column  = 0   # Amount of columns

file = open('weather.nominal.arff', 'r')  # File of study

file.readline() # Jump one line
file.readline() # Jump one line

# Reads the metadata's attributes:
# [0] outlook
# [1] temperature
# [2] humidity
# [3] windy
# [4] play
def readmetadata():
  column  = 0   # Amount of columns

  while True:
    line = file.readline()    # Take a line
  
    if re.match('\n', line):  # If is a empty line
      file.readline()         # Jump one line
      break                   # Stop this operation
    else:
      line  = line.strip()    # Remove "\n" caracter
      num   = line.find('{')  # Search the begin of the metadatas
      line  = line[num+1:-1]  # Extract the metadatas until before "}"
  
      att.append(line.split(', '))  # Transform the string in a list
      column = column + 1           # Adds a column
  return column

# Reads and storage the informations
# data[] == [outlook, temperature, humidity, windy, play]
def readdata():
  while True:
    line = file.readline()  # Take a line of archive
                            # This line is after of "@data"
    
    if len(line) == 0:      # If arrived at the end of file
      break                 # Stop this operation
    else:
      line = line.strip()           # Remove "\n" caracter
      data.append(line.split(','))  # Transform the string in a list

# Search if any element of the currentdel are equals the item
def isdeleted(currentdel, item):
  if all( ( x in item for x in currentdel ) ):
     return True
  else:
    return False

# Function that do the combination in a list
# All elements of [1] -> [2] and [2] - > [3]...
def combination(elements, number):
  newlist = []  # List that will be returned
  count   = 0   # Control the first while

  while count < len(elements) - 1:  # Until the penultimate
    sublist1  = elements[count]     # Receive the frist sublist
    sublist2  = elements[count+1]   # Receive the secound firstlist
    templist1 = []                  # Hold the value of the templelist2

    for word1 in sublist1:    # Iterate all sublist1
      for word2 in sublist2:  # Iterate all sublist2
        if number == 0:       # If is the first time that use this function
          templist2 = [word1] + [word2] # Save the words how lists and sum
        else:
          templist2 = word1 + word2     # Save the words and sum
        templist1.append(list ( set(templist2) ) )  # Appends the new list
                                                    # and remove repeated itens
    newlist.append(templist1)   # Appends the templist1
    count = count + 1           # Update the value of the count variable
  return newlist                # Returns the list generated

column = readmetadata() # Call to the readmetada's function
readdata()              # Call to the readdata's function
file.close()            # Close the file

teste = combination(att, 0)
#teste = combination(teste, 1)
print teste
