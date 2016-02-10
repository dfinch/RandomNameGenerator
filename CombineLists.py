########################################################
### File: CombineLists.py                            ###
### Author: dfinch                                   ###
### Date: 2/9/2016                                   ###
### Usage: CombineLists.py [inFile1 inFile2 outFile] ###
### Synopsis: Inputs two line-delimited text lists   ###
###           and creates a combined, non-repeating  ###
###           lexicographically-sorted, list from    ###
###           their collective contents.             ###
########################################################

import sys
import os.path

inFile1 = ""
inFile2 = ""
outFile = ""

list1 = []
list2 = []
set1 = set()
set2 = set()
outList = []

# Get the in and out files
if(len(sys.argv) != 4):
    inFile1 = raw_input("List 1 File: ")
    inFile2 = raw_input("List 2 File: ")
    outFile = raw_input("Output file: ")
else:
    inFile1 = sys.argv[1]
    inFile2 = sys.argv[2]
    outFile = sys.argv[3]

# Check for the existence of the input files
if(not os.path.isfile(inFile1)):
    print("CombineLists.py - Error: File " + inFile1 + " does not exist.")
    sys.exit(1)

if(not os.path.isfile(inFile2)):
    print("CombineLists.py - Error: File " + inFile2 + " does not exist.")
    sys.exit(1)

print("Combining lists...")

# Open both files for reading, sequentially, and populate the corresponding lists.
in1 = open(inFile1, "r")
for line in in1:
    list1.append(line.lstrip().rstrip().lower())
in1.close()

in2 = open(inFile2, "r")
for line in in2:
    list2.append(line.lstrip().rstrip().lower())
in2.close()

# Add both lists to a set, and then create outList form the sorted set
set1.update(list1)
set2.update(list2)
outList = sorted(list(set1 | set2), key=str.lower)

print("Found " + str(len(set1.symmetric_difference(set2))) + " unique elements.")
print("Found " + str(len(set1.intersection(set2))) + " elements that were present in both lists.")

# Output the outList into the desired file
out = open(outFile, "w")
for entry in outList:
    out.write(entry+"\n")
out.close()

print("Successfully combined lists into file: " + outFile + "    Exiting.")
