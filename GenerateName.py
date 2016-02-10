########################################################
### File: GenerateName.py                            ###
### Author: dfinch                                   ###
### Date: 2/9/2016                                   ###
### Usage: GenerateName.py nameCount list1File [...] ###
### Synopsis: Inputs a series of lists and chooses   ###
###           a random word from each list to add to ###
###           the randomly-generated name.           ###
########################################################

import sys
import os.path
import random

inFileList = []
wordListList = []
nameList = []
nameCount = 0

# Ensure proper program usage
if(len(sys.argv) < 3):
    print("GenerateName.py - Usage: GenerateName.py nameCount list1File [...]") 
    sys.exit(1)

# Ensure that a valid number is supplied for nameCount
try:
    nameCount = int(sys.argv[1])
    #print("sys.argv[1] = " + sys.argv[1])
    #print("nameCount = " + nameCount)
except ValueError:
    print("GenerateName.py - Error: nameCount supplied is not a valid number")
    sys.exit(1)

print("nc = " + str(nameCount))

# Check for the existence of all the input files
inFileList = sys.argv[2:]
for fn in inFileList:
    if(not os.path.isfile(fn)):
        print("GenerateName.py - Error: File " + fn + " does not exist.")
        sys.exit(1)

print("Reading from word lists...")

# Read all list files, and populate the corresponding lists
for fn in inFileList:
    inFile = open(fn, "r")
    tempList = []
    for line in inFile:
        tempList.append(line.lstrip().rstrip().lower())
    inFile.close()
    wordListList.append(tempList)

print("Generating names...")

# Pull a word from each list sequentially to generate names, and print out the list of names
for n in range(nameCount):
    tempName = ""
    for L in wordListList:
        word = random.choice(L)
        # Make the first letter of each word uppercase for clarity
        word = word[0].upper() + word[1:]
        tempName += word
    nameList.append(tempName)

print("Done! Names listed below:")
print("_______________________________________")

# Print all the names in the nameList
for name in nameList:
    print(name)
