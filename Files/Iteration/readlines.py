"""
Iterating over files.
"""

# Using readlines()
#  readlines creates a list of strings
#  that you can iterate over

datafile1 = open("the_idiot.txt", "rt")

for line in datafile1.readlines():
    print(line)

datafile1.close()
