# RandomNameGenerator
Program to create random names from several lists of words
In order to create random names, run GenerateName.py as described by the Usage section below.
The python files in this project were built using Python version 2.7.

Files:
	GenerateName.py    - Generate a number of names from the given lists of words
	CombineLists.py    - Helper program to combine two files of newline-delimted lists into a new list file
	adjectives.txt     - List of adjectives
	colors.txt         - List of colors
	singularNouns.txt  - Aggregate list of singular nouns

Program Usage:
	python GenerateName.py nameCount list1File [...]
	python CombineLists.py [inFile1 inFile2 outFile]
	
	(If you've added the Python directories to your system path variable, you can omit "python" from the lines above)
