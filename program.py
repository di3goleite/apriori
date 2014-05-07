#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Call to the libraries
import re   # Regular Expression

att           = []  # Metadata of attributes
data          = []  # Data of archive
newitems      = []  # items that have min support
newdelitems   = []  # New deleted items
column        = 0   # Amount of columns
minsupp       = argv[1] # Reiceve this min support how arg

file = open('weather.nominal.arff', 'r')  # File of study

file.readline() # Jump one line
file.readline() # Jump one line

# Reads the metadata's attributes:
# [0] outlook
# [1] temperature
# [2] humidity
# [3] windy
# [4] play
def read_metadata():
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
def read_data():
  while True:
    line = file.readline()  # Take a line of archive
                            # This line is after of "@data"
    
    if len(line) == 0:      # If arrived at the end of file
      break                 # Stop this operation
    else:
      line = line.strip()           # Remove "\n" caracter
      data.append(line.split(','))  # Transform the string in a list

# Search if any element of the currentdel are equals the item
def is_deleted(currentdel, item):
  if all( ( x in item for x in currentdel ) ):
     return True
  else:
    return False

# Calculate list's support of the items
# newitems = list of new items without calculated support
# data = is a database of informations tha is used
# minsupp = support minimum
def calc_support(newitems, data, minsupp):
  support = []
  column  = 0
  line    = 0
  size    = len(data)

  while column < len(newitems)-1:
    while line < len(newitems[column]-1):
      count = 0
      for x in data:
        if x in newitems[column][line]:
          count = count + 1
      support[column][line].append(count/size)
  return support  # Return a list equals newitems list's positions
                  # with the support of all items.

# Function that do the combination in a list
# All elements of [1] -> [2] and [2] - > [3]...
def combination(elements, newdelitems, number):
  currentdel = newdelitems  # currentdel is the older newdelitems
  newdelitems = []          # 
  newlist = []              # List that will be returned
  count   = 0               # Control the first while

  while count < len(elements) - 1:  # Until the penultimate
    sublist1  = elements[count]     # Receive the frist sublist
    sublist2  = elements[count+1]   # Receive the secound firstlist
    templist1 = []                  # Hold the value of the templelist2

    for word1 in sublist1:    # Iterate all sublist1
      for word2 in sublist2:  # Iterate all sublist2
        if number == 0:       # If is the first time that use this function
          templist2 = [word1] + [word2] # Save the words how lists and sum
          templist1.append(list ( set(templist2) ) )  # Appends the new list
        else:
          templist2 = word1 + word2     # Save the words and sum
          if (is_deleted(currentdel, templist2)):
            newdelitems.append(templist2)
            break
          else:
            templist1.append(list ( set(templist2) ) )  # Appends the new list
                                                    # and remove repeated items
    newlist.append(templist1)   # Appends the templist1
    count = count + 1           # Update the value of the count variable
  return newlist                # Returns the list generated
  # Return too newdelitems

column = read_metadata() # Call to the readmetada's function
read_data()              # Call to the read_data's function
file.close()            # Close the file

#teste = combination(data, newdelitems, 0)
#print teste[0]
